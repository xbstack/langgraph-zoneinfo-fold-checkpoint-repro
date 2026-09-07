# Version matrix

| Date | Source | Version / commit | Result |
|---|---|---|---|
| 2026-09-07 | langchain-ai/langgraph | `81bf17b23` (`langgraph-checkpoint` 4.2.0 package metadata) | Reproduced: `ZoneInfo` becomes fixed-offset `datetime.timezone`, DST +1 day result shifts by one hour, `fold=1` becomes `0` |

This fixture intentionally pins the upstream commit referenced by LangGraph issue #8826. It does not claim every released package or future commit has the same behavior.
