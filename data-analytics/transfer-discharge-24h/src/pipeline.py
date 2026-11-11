"""Pipeline: raw template export -> clean -> metric -> outputs.

Usage:
    python -m src.pipeline --input data/adt_transfer_export.xls --config config/metric.yaml --out output/
    python -m src.pipeline --input data/transfer_events.csv --config config/metric.yaml --out output/ --no-clean
    python -m src.pipeline --input ... --dedup count_all      # compare against deduped
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from dataclasses import replace
from datetime import datetime

from .config import load_config
from .clean import clean
from .metric import VALID_DEDUP_RULES, TransferEvent, compute

CLEANED_COLS = {"patient_id", "csn", "visit_id", "from_unit", "to_unit",
                "eff_ts", "disch_ts", "delta_hours"}


def _parse_ts(value: str) -> datetime:
    value = (value or "").strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


def load_cleaned(path: str) -> list:
    events = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = CLEANED_COLS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"input missing required columns: {sorted(missing)}")
        for i, row in enumerate(reader, start=2):
            eff = _parse_ts(row["eff_ts"])
            disch = _parse_ts(row["disch_ts"])
            events.append(TransferEvent(
                patient_id=row["patient_id"].strip(),
                csn=row["csn"].strip(),
                visit_id=row["visit_id"].strip(),
                from_unit=row["from_unit"].strip(),
                to_unit=row["to_unit"].strip(),
                eff_ts=eff,
                disch_ts=disch,
                delta_hours=float(row.get("delta_hours")
                                  or (disch - eff).total_seconds() / 3600.0),
            ))
    return events


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Discharges within N h of transfer")
    ap.add_argument("--input", required=True,
                    help="raw template export (.xls/.xlsx/.csv) or cleaned CSV")
    ap.add_argument("--config", default=None, help="config/metric.yaml")
    ap.add_argument("--out", default="output", help="output directory")
    ap.add_argument("--no-clean", action="store_true",
                    help="treat input as already-cleaned transfer_events.csv")
    ap.add_argument("--dedup", choices=VALID_DEDUP_RULES, default=None,
                    help="override dedup rule (closest_to_discharge is the default)")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    if args.dedup:
        cfg = replace(cfg, dedup_rule=args.dedup)
    os.makedirs(args.out, exist_ok=True)

    cleaned_path = None
    if args.no_clean:
        cleaned_path = args.input
    else:
        ext = args.input.lower().rsplit(".", 1)[-1] if "." in args.input else ""
        if ext in ("xls", "xlsx"):
            raw = True
        else:
            with open(args.input, newline="", encoding="utf-8-sig") as _fh:
                cols = {c.strip().lower() for c in _fh.readline().replace("\r", "").split(",")}
            raw = bool(cols & {"eff date time", "disch date/time", "from unit", "to unit"}) \
                and not (CLEANED_COLS <= cols)
        if raw:
            cleaned_path = os.path.join(args.out, "transfer_events.csv")
            stats = clean(args.input, cleaned_path,
                          from_units=cfg.from_units or ("RBMC NT ICU", "RBMC CV ICU"),
                          timezone=cfg.timezone)
            print(json.dumps({"clean_stats": stats, "cleaned_to": cleaned_path,
                              "timezone": cfg.timezone}, indent=2))
        else:
            cleaned_path = args.input

    events = load_cleaned(cleaned_path)
    result = compute(events, cfg)

    summary_path = os.path.join(args.out, "summary.json")
    with open(summary_path, "w", encoding="utf-8") as fh:
        json.dump(result.to_dict(), fh, indent=2)

    matches_path = os.path.join(args.out, "matches.csv")
    with open(matches_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["patient_id", "csn", "from_unit", "to_unit",
                    "transfer_ts", "discharge_ts", "delta_hours"])
        for m in result.matches:
            w.writerow([m.patient_id, m.csn, m.from_unit, m.to_unit,
                        m.transfer_ts.isoformat(), m.discharge_ts.isoformat(),
                        f"{m.delta_hours:.3f}"])

    by_day_path = os.path.join(args.out, "by_day.csv")
    with open(by_day_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "encounters_total", "discharges_within_window", "rate"])
        for d, v in sorted(result.by_day.items()):
            rate = (v["within"] / v["total"]) if v["total"] else 0.0
            w.writerow([d.isoformat(), v["total"], v["within"], f"{rate:.4f}"])

    print(json.dumps({
        "total_rows": result.total_rows,
        "encounters_total": result.encounters_total,
        "transfers_qualifying": result.transfers_qualifying,
        "discharges_within_window": result.discharges_within_window,
        "rate": round(result.rate, 6),
        "window_hours": cfg.window_hours,
        "dedup_rule": cfg.dedup_rule,
        "timezone": cfg.timezone,
        "outputs": [summary_path, matches_path, by_day_path],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
