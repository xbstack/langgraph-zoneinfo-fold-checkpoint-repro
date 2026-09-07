# LangGraph ZoneInfo / fold checkpoint round-trip repro

Independent XBSTACK reproduction of LangGraph issue #8826.

## Problem

A zone-aware `datetime` serialized through `JsonPlusSerializer` can deserialize with the same instant but with a fixed UTC offset instead of the original `zoneinfo.ZoneInfo`. The `fold` bit is also lost. That means time arithmetic crossing a DST boundary can produce a different wall-clock result after checkpoint restore without raising an error.

## Environment

- Date tested: 2026-09-07
- Python: 3.10
- Upstream commit: `langchain-ai/langgraph@81bf17b23`
- Package built from `libs/checkpoint`: `langgraph-checkpoint` 4.2.0 metadata
- External API/model calls: none

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python repro.py
```

Expected output ends with `REPRODUCED` and shows:

- `ZoneInfo('America/New_York')` becomes a fixed-offset `datetime.timezone`;
- adding one day across the March DST boundary changes `09:00` into `10:00` after restore;
- `fold=1` becomes `fold=0`.

See `logs/repro-2026-09-07.txt` for the captured XBSTACK run.

## Scope

This repository reproduces the serializer behavior only. It does not claim that all LangGraph releases are affected, that upstream has accepted a specific fix, or that historical checkpoints can recover timezone information that was never stored.

Upstream: https://github.com/langchain-ai/langgraph/issues/8826
