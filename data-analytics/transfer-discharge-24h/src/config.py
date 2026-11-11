"""Configuration loading for the metric.

Reads config/metric.yaml. Requires PyYAML; falls back to a tiny flat-schema
parser if PyYAML is unavailable so the pipeline stays runnable in a bare env.
"""
from __future__ import annotations

from typing import Optional

from .metric import MetricConfig


def _flat_yaml_load(text: str) -> dict:
    """Parse the flat schema used in config/metric.yaml (scalars + inline lists)."""
    out: dict = {}
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            out[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
        elif val.lower() in ("null", "none", "~", ""):
            out[key] = None
        elif val.lower() in ("true", "false"):
            out[key] = val.lower() == "true"
        else:
            try:
                out[key] = float(val) if "." in val else int(val)
            except ValueError:
                out[key] = val.strip("'\"")
    return out


def load_config(path: Optional[str] = None) -> MetricConfig:
    if not path:
        return MetricConfig()
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text) or {}
    except ImportError:
        data = _flat_yaml_load(text)

    return MetricConfig(
        window_hours=float(data.get("window_hours", 24.0)),
        min_delta_hours=float(data.get("min_delta_hours", 0.0)),
        from_units=tuple(data.get("from_units") or MetricConfig.from_units),
        exclude_same_location=bool(data.get("exclude_same_location", True)),
        dedup_rule=str(data.get("dedup_rule") or MetricConfig.dedup_rule),
        timezone=str(data.get("timezone") or MetricConfig.timezone),
        max_back_date_hours=(float(data["max_back_date_hours"])
                             if data.get("max_back_date_hours") is not None else None),
    )
