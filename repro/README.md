# Reproduction fixture

Run the repository-root `repro.py` after installing `requirements.txt`. The root script is the canonical minimal fixture used for the captured 2026-09-07 result.

The expected failure shape is:

- `zoneinfo.ZoneInfo` deserializes as a fixed-offset `datetime.timezone`;
- DST-crossing wall-clock arithmetic changes after restore;
- `fold=1` is not preserved.
