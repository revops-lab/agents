"""
validate_fields.py : check proposed CRM deal values before anything is written.

Reads the field list from ../references/crm-fields.json, so it works with any CRM
set-up. It never writes to the CRM. It only validates and orders values so the
seller can review them against their deal screen.

Usage:
    from validate_fields import validate, order_for_review
    clean, problems = validate({"pain_severity": "medium", "next_step_date": "2026-11-03"})
    rows = order_for_review(clean)

Run directly for a self-check:
    python validate_fields.py
"""

import json
from datetime import datetime
from pathlib import Path

CONFIG = Path(__file__).resolve().parent.parent / "references" / "crm-fields.json"


def load_config(path=CONFIG):
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg["fields"], set(cfg.get("never_write", [])), cfg.get("display_order", list(cfg["fields"]))


def _match_option(value, options):
    v = str(value).strip().lower()
    return next((o for o in options if o.lower() == v), None)


def _is_number(value):
    try:
        float(str(value).replace(",", "").strip())
        return True
    except (TypeError, ValueError):
        return False


def _is_iso_date(value):
    try:
        datetime.strptime(str(value).strip(), "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False


def validate(values, path=CONFIG):
    """Return (clean, problems). Blanks are dropped on purpose: unsupported fields stay empty."""
    fields, never_write, _ = load_config(path)
    clean, problems = {}, []

    for name, value in values.items():
        if value is None or str(value).strip() == "":
            continue
        spec = fields.get(name)
        if name in never_write or spec is None:
            problems.append(f"'{name}' is not a writable field; skipping.")
            continue
        if spec.get("write") is False:
            problems.append(f"'{name}' is display-only and is never set by this skill.")
            continue

        kind = spec["type"]
        if kind == "enum":
            match = _match_option(value, spec["options"])
            if match is None:
                problems.append(f"'{name}' value '{value}' is not allowed. Use one of: {', '.join(spec['options'])}.")
            else:
                clean[name] = match
        elif kind == "number":
            if _is_number(value):
                clean[name] = str(value).replace(",", "").strip()
            else:
                problems.append(f"'{name}' must be a number, got '{value}'.")
        elif kind == "date":
            if _is_iso_date(value):
                clean[name] = str(value).strip()
            else:
                problems.append(f"'{name}' must be a date as YYYY-MM-DD, got '{value}'.")
        else:
            clean[name] = str(value).strip()

    return clean, problems


def order_for_review(values, path=CONFIG):
    """Return rows (label, internal_name, value) in deal-screen order, including display-only fields."""
    fields, _, order = load_config(path)
    rows = []
    for name in order:
        spec = fields.get(name, {})
        if spec.get("write") is False:
            rows.append((spec.get("label", name), name, "not set by this skill"))
        else:
            rows.append((spec.get("label", name), name, values.get(name, "insufficient info")))
    return rows


if __name__ == "__main__":
    sample = {
        "pain_severity": "medium",            # normalises to Medium
        "champion_strength": "developing",    # normalises to Developing
        "next_step_date": "2026-11-03",
        "critical_event_date": "next spring", # not a date: problem
        "forecast_category": "Maybe",         # not an option: problem
        "quantified_value": "",               # blank: dropped
        "owner": "Sam",                       # display-only: problem
    }
    clean, problems = validate(sample)
    print("CLEAN:", clean)
    print("PROBLEMS:")
    for p in problems:
        print(" -", p)
    print("\nREVIEW ORDER:")
    for i, (label, name, value) in enumerate(order_for_review(clean), 1):
        print(f"{i:>2}. {label} ({name}): {value}")
