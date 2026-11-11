-- 02_24h_flag.sql
-- Reference projection of src/metric.py for the SAME-ROW model, including the
-- requester's closest-to-discharge dedup rule.
--
-- Input: template export rows (or a table loaded from it) with columns
--   [Patient ID], [CSN], [From Unit], [To Unit], [Eff Date Time], [Disch Date/Time].
-- Timestamps are PDT wall-clock (America/Los_Angeles); both come from the same
-- export so DATEDIFF is zone-consistent.
--
-- The Python core is the reference; this SQL must agree with it line-for-line.
-- On disagreement, fix THIS file (core wins).
--
-- Parameterize:
--   @window_hours = 24
--   from-unit filter = ('RBMC NT ICU','RBMC CV ICU')   -- [FROM RWB: from_unit_filter]

DECLARE @window_hours FLOAT = 24.0;

WITH src AS (
    SELECT
        [Patient ID]        AS patient_id,
        [CSN]               AS csn,
        COALESCE(NULLIF([CSN], ''), CONVERT(varchar(23), [Eff Date Time], 126)) AS enc_key,
        [From Unit]         AS from_unit,
        [To Unit]           AS to_unit,
        [Eff Date Time]     AS eff_ts,
        [Disch Date/Time]   AS disch_ts
    FROM ADT_TRANSFER_EXPORT   -- [FROM RWB: export table/view, or temp load of the .xls]
),
scored AS (
    SELECT *,
           CAST(DATEDIFF(second, eff_ts, disch_ts) AS FLOAT) / 3600.0 AS delta_hours
    FROM src
),
qual AS (
    SELECT * FROM scored
    WHERE disch_ts >= eff_ts
      AND delta_hours >= 0
      AND delta_hours <= @window_hours
      AND NOT (from_unit IS NOT NULL AND to_unit IS NOT NULL AND from_unit = to_unit)
      AND from_unit IN ('RBMC NT ICU','RBMC CV ICU')
),
ranked AS (
    -- closest to discharge wins; tie-break latest eff_ts (matches _pick())
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY patient_id, enc_key
                              ORDER BY delta_hours ASC, eff_ts DESC) AS rn
    FROM qual
),
encounters AS (
    SELECT patient_id, enc_key FROM src GROUP BY patient_id, enc_key
)
SELECT
    (SELECT COUNT(*) FROM src)                                        AS total_rows,
    (SELECT COUNT(*) FROM encounters)                                 AS encounters_total,
    (SELECT COUNT(*) FROM qual)                                       AS transfers_qualifying,
    (SELECT COUNT(*) FROM ranked WHERE rn = 1)                        AS discharges_within_window,
    CAST((SELECT COUNT(*) FROM ranked WHERE rn = 1) AS FLOAT)
      / NULLIF((SELECT COUNT(*) FROM encounters), 0)                  AS rate;

-- Audit detail (the representative transfer per counted encounter):
-- SELECT * FROM ranked WHERE rn = 1 ORDER BY disch_ts;
