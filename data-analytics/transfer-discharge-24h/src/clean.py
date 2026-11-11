"""Cleaner for the raw ADT-transfer export.

The template "Modify ADT Transfers [Location]" (Report Model M24047, ID [100432])
exports ONE ROW PER TRANSFER that already carries both the transfer effective
time (`Eff Date Time`) AND the encounter's discharge time (`Disch Date/Time`) on
the same row. So the 24h clock is a same-row comparison, not a cross-event join.

Clean = drop the display-only columns, parse `Eff Date Time` + `Disch Date/Time`,
and keep rows where a real, in-window transfer exists for a discharge to be
measured against.

Input: an .xls/.xlsx/.csv export of the template. Output: `transfer_events.csv`
with exactly the columns the metric core consumes.

`[FROM RWB: <slot>]` tokens are filled from the export; see
docs/rwb-datasource.md and docs/template-config.md.
"""
from __future__ import annotations

import csv
import re
from datetime import datetime
from typing import Iterable, Optional
from zoneinfo import ZoneInfo

# Template export columns (per the requester's schema) — verbatim.
# Display-only columns the metric never needs:
DISPLAY_ONLY_COLS = (
    "Name", "Attending", "From Room", "From Bed", "To Room", "To Bed",
    "From Class", "To Class", "From Service", "To Service", "Discharge Provider",
)
# Patient/visit identifiers (synthetic-able; MRN/Name are PHI-adjacent -> gitignored).
# MRN and Name are NOT needed for the metric (Patient ID + CSN identify the visit);
# they are dropped by the cleaner to keep the working file lean.
IDENTIFIER_COLS = ("MRN", "CSN", "Name", "Patient ID", "DAT")

# Columns the metric consumes.
KEEP_COLS = (
    "Patient ID", "CSN", "From Unit", "To Unit",
    "Eff Date Time", "Disch Date Time",
)

# [FROM RWB: template_id] -> "Modify ADT Transfers [Location]" (Report Model M24047 [100432])
TEMPLATE_NAME = "Modify ADT Transfers [Location]"
TEMPLATE_MODEL = "M24047"
TEMPLATE_ID = "100432"

# [FROM RWB: effective_date_from] / [to] -> the template's report window.
DEFAULT_EFFECTIVE_FROM = "2025-11-10"
DEFAULT_EFFECTIVE_TO = "2026-11-09"

# [FROM RWB: previous_event_item] -> criterion 2006 = "Previous Event for the
# encounter"; [FROM RWB: linked_item] -> item 50 (the unit criterion it links to).
PREVIOUS_EVENT_ITEM = "2006"
LINKED_ITEM = "50"

# [FROM RWB: from_unit_filter] -> transfers whose PREVIOUS event was in an ICU.
# [FROM RWB: reporting_base_class] -> Inpatient OR / Observation.
# [FROM RWB: revenue_location] -> RIVERBEND MEDICAL CENTER.
ICU_FROM_UNITS = ("RBMC NT ICU", "RBMC CV ICU")
REPORTING_BASE_CLASS = ("Inpatient OR", "Observation")
REVENUE_LOCATION = "RIVERBEND MEDICAL CENTER"

_TS_TOKEN = re.compile(r"(\d{1,2})[-/](\d{1,2})[-/](\d{2,4})(?:\s+(\d{1,2}):(\d{2})(?::(\d{2}))?)?\s*([AaPp][Mm])?")


def _parse_ts(value: str) -> Optional[datetime]:
    """Parse `Eff Date Time` / `Disch Date/Time` cells.

    Accepts ISO (`2026-01-10T08:00:00`), Excel-style `MM/DD/YYYY [hh:mm[:ss][AM/PM]]`,
    and epoch floats (Excel serial dates). Returns None when unparseable/blank.
    """
    if value is None:
        return None
    value = str(value).strip()
    if not value or value.upper() in ("N/A", "NA", "NONE", "--"):
        return None
    # ISO first (already normalized or exported that way)
    try:
        v = value[:-1] + "+00:00" if value.endswith("Z") else value
        return datetime.fromisoformat(v)
    except ValueError:
        pass
    m = _TS_TOKEN.search(value)
    if m:
        mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if y < 100:
            y += 2000
        hh = int(m.group(4) or 0)
        mm = int(m.group(5) or 0)
        ss = int(m.group(6) or 0)
        ampm = (m.group(7) or "").upper()
        if ampm == "PM" and hh < 12:
            hh += 12
        elif ampm == "AM" and hh == 12:
            hh = 0
        try:
            return datetime(y, mo, d, hh, mm, ss)
        except ValueError:
            return None
    # Excel serial date (epoch float)
    try:
        serial = float(value)
    except ValueError:
        return None
    if 20000 < serial < 90000:  # ~1954..2045 sanity band
        from datetime import timedelta
        return datetime(1899, 12, 30) + timedelta(days=serial)
    return None


def _to_zone(dt: Optional[datetime], tz_name: str) -> Optional[datetime]:
    """Attach the source time zone to a parsed timestamp.

    The export stores wall-clock local time (PDT at Riverbend). Naive datetimes
    are assumed to already be in that zone; aware ones are converted to it, so
    every comparison in the metric runs on one tz-aware basis.
    """
    if dt is None:
        return None
    zone = ZoneInfo(tz_name)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=zone)
    return dt.astimezone(zone)


def _read_table(path: str) -> Iterable[dict]:
    """Yield dicts from an .xls/.xlsx/.csv export (columns keyed by header name)."""
    ext = path.lower().rsplit(".", 1)[-1] if "." in path else ""
    if ext in ("csv", "txt"):
        with open(path, newline="", encoding="utf-8-sig") as fh:
            yield from csv.DictReader(fh)
        return
    if ext in ("xls", "xlsx"):
        try:
            import pandas as pd
        except ImportError as exc:
            raise ImportError(
                "pandas is required to read .xls/.xlsx exports. "
                "pip install pandas (and xlrd for .xls). Or export as CSV."
            ) from exc
        df = pd.read_excel(path, dtype=str).fillna("")
        for row in df.to_dict(orient="records"):
            yield {k: ("" if v is None else str(v)) for k, v in row.items()}
        return
    raise ValueError(f"unsupported export type: {ext!r} (expected .xls/.xlsx/.csv)")


def normalize_headers(raw_cols: Iterable[str]) -> dict:
    """Map raw header spellings -> canonical KEEP_COLS keys (case/whitespace tolerant)."""
    canon = {
        "patient id": "Patient ID", "patientid": "Patient ID", "patient": "Patient ID",
        "csn": "CSN", "contact serial number": "CSN",
        "from unit": "From Unit", "to unit": "To Unit",
        "eff date time": "Eff Date Time", "eff date/time": "Eff Date Time",
        "eff datetime": "Eff Date Time", "effective date time": "Eff Date Time",
        "disch date/time": "Disch Date Time", "disch date time": "Disch Date Time",
        "discharge date/time": "Disch Date Time",
    }
    return {c: canon.get(str(c).strip().lower(), str(c).strip()) for c in raw_cols}


def clean(
    path: str,
    out_path: str,
    from_units: tuple = ICU_FROM_UNITS,
    require_from_icu: bool = True,
    drop_display_only: bool = True,
    window_hours: Optional[float] = None,
    timezone: str = "America/Los_Angeles",
) -> dict:
    """Read the raw template export -> write normalized `transfer_events.csv`.

    Returns a stats dict. `window_hours` (optional) only TRIMS rows whose
    Disch-Eff gap exceeds the window (a pre-filter); the metric core still
    enforces the window, so this is optional and defaults to off.
    """
    stats = {"rows_in": 0, "rows_out": 0, "no_discharge": 0, "out_of_window": 0,
             "not_from_icu": 0, "bad_timestamps": 0}
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["patient_id", "csn", "visit_id", "from_unit", "to_unit",
                    "eff_ts", "disch_ts", "delta_hours"])
        for i, row in enumerate(_read_table(path), start=2):
            stats["rows_in"] += 1
            hdr = normalize_headers(list(row.keys()))
            rev = {v: c for c, v in hdr.items()}
            g = lambda k: str(row.get(rev.get(k, ""), "") or "").strip()
            eff = _to_zone(_parse_ts(g("Eff Date Time")), timezone)
            disch = _to_zone(_parse_ts(g("Disch Date Time")), timezone)
            if eff is None or disch is None:
                stats["bad_timestamps"] += 1
                continue
            fu = (g("From Unit") or "").strip()
            tu = (g("To Unit") or "").strip()
            if require_from_icu and from_units and fu not in from_units:
                stats["not_from_icu"] += 1
                continue
            delta_h = (disch - eff).total_seconds() / 3600.0
            if disch < eff:
                stats["out_of_window"] += 1
                continue
            if window_hours is not None and delta_h > window_hours:
                stats["out_of_window"] += 1
                continue
            # encounter key: Patient ID + CSN (Epic contact serial = the visit).
            # Fallback to eff when CSN is missing so a row still gets a key.
            pid = (g("Patient ID") or "").strip()
            csn = (g("CSN") or "").strip()
            visit_id = f"{pid}|{csn}" if csn else f"{pid}|{eff.isoformat()}"
            w.writerow([pid, csn, visit_id, fu, tu, eff.isoformat(),
                        disch.isoformat(), f"{delta_h:.3f}"])
            stats["rows_out"] += 1
    return stats
