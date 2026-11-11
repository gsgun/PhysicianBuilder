-- 03_daily_rollup.sql
-- Daily series for the BI view. Same-row model + closest-to-discharge dedup as 02.
-- Keyed on the discharge date, matching src/metric.py by_day. Timestamps PDT.

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
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY patient_id, enc_key
                              ORDER BY delta_hours ASC, eff_ts DESC) AS rn
    FROM qual
),
best AS (
    SELECT * FROM ranked WHERE rn = 1
),
encounter_days AS (
    -- every encounter in the export, keyed to its discharge date
    SELECT patient_id, enc_key, CAST(MAX(disch_ts) AS DATE) AS day
    FROM src
    GROUP BY patient_id, enc_key
)
SELECT
    d.day                                                   AS day,
    COUNT(*)                                                AS encounters_total,
    SUM(CASE WHEN b.patient_id IS NOT NULL THEN 1 ELSE 0 END) AS discharges_within_window,
    CAST(SUM(CASE WHEN b.patient_id IS NOT NULL THEN 1 ELSE 0 END) AS FLOAT)
      / NULLIF(COUNT(*), 0)                                 AS rate
FROM encounter_days d
LEFT JOIN best b
  ON b.patient_id = d.patient_id AND b.enc_key = d.enc_key
GROUP BY d.day
ORDER BY d.day;
