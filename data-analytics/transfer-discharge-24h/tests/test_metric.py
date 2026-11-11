"""Unit tests for the discharge-within-window-of-transfer metric (stdlib unittest).

Model: same-row template export (Eff Date Time + Disch Date/Time on one row).
Multi-transfer rule: keep the transfer closest to discharge per encounter
(Patient ID + CSN); count each encounter once.

Run from the project root:
    python3 -m unittest discover -s tests -v
"""
import os
import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from src.metric import TransferEvent, MetricConfig, compute
from src.clean import clean

PDT = ZoneInfo("America/Los_Angeles")
FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "sample_transfer_events.csv")
OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output", "_cleaned_test_out.csv")


def _dt(s):
    return datetime.fromisoformat(s).replace(tzinfo=PDT)


def E(pid, cid, fu, tu, eff, disch):
    """Shortcut for a cleaned transfer row (encounter key = pid|csn)."""
    eff_dt, disch_dt = _dt(eff), _dt(disch)
    delta = (disch_dt - eff_dt).total_seconds() / 3600.0
    return TransferEvent(
        patient_id=pid, csn=cid, visit_id=f"{pid}|{cid}",
        from_unit=fu, to_unit=tu,
        eff_ts=eff_dt, disch_ts=disch_dt, delta_hours=delta,
    )


class TestMetric(unittest.TestCase):
    def setUp(self):
        self.cfg = MetricConfig()  # 24h, closest_to_discharge, two RBMC ICUs, PDT

    def _events(self):
        return [
            E("P001", "C001", "RBMC NT ICU", "4NW", "2026-01-10T08:00:00", "2026-01-10T20:00:00"),   # 12h -> count
            E("P002", "C002", "RBMC CV ICU", "5E", "2026-01-11T02:00:00", "2026-01-13T02:00:00"),   # 48h -> out
            E("P003", "C003", "RBMC NT ICU", "RBMC NT ICU", "2026-01-12T10:00:00", "2026-01-12T14:00:00"),  # same-loc no-op
            E("P004", "C004", "RBMC CV ICU", "ICU STAFF", "2026-01-13T22:00:00", "2026-01-13T18:00:00"),  # disch before transfer
            E("P005", "C005", "RBMC NT ICU", "6W", "2026-01-14T09:00:00", "2026-01-14T09:30:00"),   # 0.5h -> count
            E("P006", "C006", "RBMC CV ICU", "4NW", "2026-01-15T07:00:00", "2026-01-16T06:59:00"),   # ~23.98h -> count
            E("P007", "C007", "4NW", "RBMC NT ICU", "2026-01-16T12:00:00", "2026-01-17T12:00:00"),   # transfer INTO icu
            E("P008", "C008", "RBMC CV ICU", "5E", "2026-01-18T15:00:00", "2026-01-18T15:00:00"),   # 0h -> count
            E("P009", "C009", "RBMC NT ICU", "6W", "2026-01-19T20:00:00", "2026-01-20T20:00:00"),   # 24h boundary -> count
            E("P010", "C010", "RBMC CV ICU", "4NW", "2026-01-21T00:00:00", "2026-01-21T06:00:00"),   # 6h -> count
            # Multi-transfer encounter: two out-of-ICU transfers, same discharge.
            E("P011", "C011", "RBMC NT ICU", "4NW", "2026-01-22T06:00:00", "2026-01-22T20:00:00"),   # 14h
            E("P011", "C011", "RBMC NT ICU", "4NW", "2026-01-22T10:00:00", "2026-01-22T20:00:00"),   # 10h <- closest
        ]

    def test_rows_and_encounters(self):
        res = compute(self._events(), self.cfg)
        self.assertEqual(res.total_rows, 12)
        self.assertEqual(res.encounters_total, 11)

    def test_qualifying_pre_dedup(self):
        res = compute(self._events(), self.cfg)
        self.assertEqual(res.transfers_qualifying, 8)

    def test_within_window_dedup(self):
        res = compute(self._events(), self.cfg)
        # count: P001,P005,P006,P008,P009,P010,P011 = 7 (P011 once)
        self.assertEqual(res.discharges_within_window, 7)

    def test_rate(self):
        res = compute(self._events(), self.cfg)
        self.assertAlmostEqual(res.rate, 7 / 11)

    def test_multi_transfer_keeps_closest(self):
        res = compute(self._events(), self.cfg)
        p11 = [m for m in res.matches if m.patient_id == "P011"]
        self.assertEqual(len(p11), 1)
        self.assertAlmostEqual(p11[0].delta_hours, 10.0, places=3)
        self.assertEqual(p11[0].transfer_ts.hour, 10)

    def test_count_all_rule(self):
        cfg = MetricConfig(dedup_rule="count_all")
        res = compute(self._events(), cfg)
        self.assertEqual(res.discharges_within_window, 8)  # both P011 rows

    def test_earliest_rule(self):
        cfg = MetricConfig(dedup_rule="earliest")
        res = compute(self._events(), cfg)
        p11 = [m for m in res.matches if m.patient_id == "P011"]
        self.assertEqual(len(p11), 1)
        self.assertEqual(p11[0].transfer_ts.hour, 6)

    def test_outside_window_not_counted(self):
        res = compute(self._events(), self.cfg)
        self.assertNotIn("P002", {m.patient_id for m in res.matches})

    def test_same_location_noop_excluded(self):
        res = compute(self._events(), self.cfg)
        self.assertNotIn("P003", {m.patient_id for m in res.matches})

    def test_discharge_before_transfer_excluded(self):
        res = compute(self._events(), self.cfg)
        self.assertNotIn("P004", {m.patient_id for m in res.matches})

    def test_transfer_into_icu_not_counted(self):
        res = compute(self._events(), self.cfg)
        self.assertNotIn("P007", {m.patient_id for m in res.matches})

    def test_boundary_inclusive(self):
        res = compute(self._events(), self.cfg)
        self.assertIn("P009", {m.patient_id for m in res.matches})

    def test_empty(self):
        res = compute([], self.cfg)
        self.assertEqual(res.total_rows, 0)
        self.assertEqual(res.encounters_total, 0)
        self.assertEqual(res.rate, 0.0)

    def test_config_validation(self):
        with self.assertRaises(ValueError):
            MetricConfig(window_hours=0).validate()
        with self.assertRaises(ValueError):
            MetricConfig(dedup_rule="bogus").validate()

    def test_timezone_attached(self):
        e = self._events()[0]
        self.assertIsNotNone(e.eff_ts.tzinfo)
        self.assertEqual(str(e.eff_ts.tzinfo), "America/Los_Angeles")

    def test_fixture_roundtrip_through_clean(self):
        stats = clean(FIXTURE, OUT, from_units=self.cfg.from_units,
                      timezone=self.cfg.timezone)
        self.assertEqual(stats["rows_out"], 10)
        import csv as _csv
        evs = []
        with open(OUT, newline="", encoding="utf-8") as fh:
            for row in _csv.DictReader(fh):
                evs.append(TransferEvent(
                    patient_id=row["patient_id"], csn=row["csn"], visit_id=row["visit_id"],
                    from_unit=row["from_unit"], to_unit=row["to_unit"],
                    eff_ts=datetime.fromisoformat(row["eff_ts"]),
                    disch_ts=datetime.fromisoformat(row["disch_ts"]),
                    delta_hours=float(row["delta_hours"]),
                ))
        res = compute(evs, self.cfg)
        self.assertEqual(res.encounters_total, 9)
        self.assertEqual(res.discharges_within_window, 7)
        p11 = [m for m in res.matches if m.patient_id == "900011"]
        self.assertEqual(len(p11), 1)
        self.assertAlmostEqual(p11[0].delta_hours, 10.0, places=3)
        self.assertNotIn("900003", {m.patient_id for m in res.matches})  # same-loc no-op


if __name__ == "__main__":
    unittest.main()
