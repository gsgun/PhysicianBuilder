"""Discharges within N hours of transfer — metric core (authoritative).

Model: the RWB template export yields one row per out-of-ICU transfer; each
row carries BOTH the transfer time (`Eff Date Time`) and the same-encounter
discharge time (`Disch Date/Time`). The clock is a same-row comparison:

    delta = disch_ts - eff_ts          count if 0 <= delta <= window_hours

Multi-transfer handling (requester rule): a patient may have several
out-of-ICU transfers on one stay (e.g. ICU -> floor -> ICU -> floor). All
rows for one stay share the encounter key (Patient ID + CSN). Within an
encounter, keep only the transfer CLOSEST TO DISCHARGE (min delta;
tie-break: latest eff_ts) and count the encounter once.

Time zone: all timestamps are normalized to America/Los_Angeles (PDT) by the
cleaner; comparisons here are tz-aware.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable, Optional

VALID_DEDUP_RULES = ("closest_to_discharge", "count_all", "earliest")


@dataclass(frozen=True)
class TransferEvent:
    """One row of the cleaned ADT-transfer export."""
    patient_id: str
    csn: str                 # contact serial number = encounter id in Epic
    visit_id: str            # encounter key: f"{patient_id}|{csn}" (or |<eff> if csn empty)
    from_unit: str
    to_unit: str
    eff_ts: datetime         # Eff Date Time (tz-aware, America/Los_Angeles)
    disch_ts: datetime       # Disch Date/Time, same encounter
    delta_hours: float       # (disch_ts - eff_ts) / 3600, precomputed


@dataclass(frozen=True)
class MetricConfig:
    """Tunables. Defaults encode the requester's template + confirmations."""
    window_hours: float = 24.0
    min_delta_hours: float = 0.0
    from_units: tuple = ("RBMC NT ICU", "RBMC CV ICU")   # safety re-check
    exclude_same_location: bool = True
    dedup_rule: str = "closest_to_discharge"             # per-encounter rule
    timezone: str = "America/Los_Angeles"               # PDT; used by cleaner
    max_back_date_hours: Optional[float] = None

    def validate(self) -> None:
        if self.window_hours <= 0:
            raise ValueError("window_hours must be > 0")
        if self.min_delta_hours < 0:
            raise ValueError("min_delta_hours must be >= 0")
        if self.min_delta_hours > self.window_hours:
            raise ValueError("min_delta_hours cannot exceed window_hours")
        if self.dedup_rule not in VALID_DEDUP_RULES:
            raise ValueError(f"dedup_rule must be one of {VALID_DEDUP_RULES}")


@dataclass
class DischargeMatch:
    patient_id: str
    csn: str
    visit_id: str
    from_unit: str
    to_unit: str
    transfer_ts: datetime
    discharge_ts: datetime
    delta_hours: float


@dataclass
class MetricResult:
    total_rows: int                       # all input rows
    encounters_total: int                 # distinct encounter keys
    transfers_qualifying: int             # rows passing the window (pre-dedup)
    discharges_within_window: int         # after dedup (headline number)
    rate: float                           # within / encounters (or /rows for count_all)
    window_hours: float
    dedup_rule: str
    matches: list = field(default_factory=list)
    by_day: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "total_rows": self.total_rows,
            "encounters_total": self.encounters_total,
            "transfers_qualifying": self.transfers_qualifying,
            "discharges_within_window": self.discharges_within_window,
            "rate": round(self.rate, 6),
            "window_hours": self.window_hours,
            "dedup_rule": self.dedup_rule,
            "matches": [
                {
                    "patient_id": m.patient_id,
                    "csn": m.csn,
                    "from_unit": m.from_unit,
                    "to_unit": m.to_unit,
                    "transfer_ts": m.transfer_ts.isoformat(),
                    "discharge_ts": m.discharge_ts.isoformat(),
                    "delta_hours": round(m.delta_hours, 3),
                }
                for m in self.matches
            ],
            "by_day": {d.isoformat(): v for d, v in sorted(self.by_day.items())},
        }


def _qualifies(e: TransferEvent, cfg: MetricConfig) -> bool:
    """True if this transfer row's discharge falls within the window."""
    if e.disch_ts < e.eff_ts:                      # discharge before transfer
        return False
    if e.delta_hours < cfg.min_delta_hours:        # too close / negative
        return False
    if e.delta_hours > cfg.window_hours:           # outside window
        return False
    if (cfg.max_back_date_hours is not None
            and e.delta_hours > cfg.max_back_date_hours):
        return False
    if cfg.exclude_same_location and e.from_unit and e.to_unit \
            and e.from_unit == e.to_unit:
        return False
    if cfg.from_units and e.from_unit not in cfg.from_units:
        return False
    return True


def _pick(qual: list, cfg: MetricConfig) -> TransferEvent:
    """Choose the representative transfer for an encounter (dedup)."""
    if cfg.dedup_rule == "earliest":
        return min(qual, key=lambda e: (e.eff_ts, e.delta_hours))
    # closest_to_discharge: min delta; tie-break latest eff_ts
    return min(qual, key=lambda e: (e.delta_hours, -e.eff_ts.timestamp()))


def _to_match(e: TransferEvent) -> DischargeMatch:
    return DischargeMatch(
        patient_id=e.patient_id,
        csn=e.csn,
        visit_id=e.visit_id,
        from_unit=e.from_unit,
        to_unit=e.to_unit,
        transfer_ts=e.eff_ts,
        discharge_ts=e.disch_ts,
        delta_hours=e.delta_hours,
    )


def compute(events: Iterable[TransferEvent], cfg: MetricConfig) -> MetricResult:
    """Count encounters discharged within the window of a qualifying transfer.

    Groups rows by encounter key (visit_id), applies the window, then the
    dedup rule. Each encounter is counted at most once.
    """
    cfg.validate()

    total_rows = 0
    by_visit: dict = {}
    for e in events:
        if not isinstance(e, TransferEvent):
            raise TypeError(f"expected TransferEvent, got {type(e)!r}")
        total_rows += 1
        by_visit.setdefault(e.visit_id, []).append(e)

    matches: list = []
    within = 0
    qualifying_rows = 0
    by_day: dict = {}
    denom = len(by_visit) if cfg.dedup_rule != "count_all" else total_rows

    for vid in sorted(by_visit):
        rows = sorted(by_visit[vid], key=lambda e: (e.eff_ts, e.delta_hours))
        # All rows of an encounter share the same-encounter discharge time;
        # take the latest available (defensive against data noise).
        visit_disch = max(r.disch_ts for r in rows)
        slot = by_day.setdefault(visit_disch.date(), {"total": 0, "within": 0})
        slot["total"] += 1

        qual = [r for r in rows if _qualifies(r, cfg)]
        if not qual:
            continue
        qualifying_rows += len(qual)

        if cfg.dedup_rule == "count_all":
            matches.extend(_to_match(r) for r in qual)
            added = len(qual)
        else:
            pick = _pick(qual, cfg)
            matches.append(_to_match(pick))
            added = 1
        within += added
        slot["within"] += added

    matches.sort(key=lambda m: (m.discharge_ts, m.patient_id, m.transfer_ts))
    return MetricResult(
        total_rows=total_rows,
        encounters_total=len(by_visit),
        transfers_qualifying=qualifying_rows,
        discharges_within_window=within,
        rate=(within / denom) if denom else 0.0,
        window_hours=cfg.window_hours,
        dedup_rule=cfg.dedup_rule,
        matches=matches,
        by_day=by_day,
    )
