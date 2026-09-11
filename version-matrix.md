# Version matrix

| Date | Source | Version / commit | Result |
|---|---|---|---|
| 2026-09-07 | langchain-ai/langgraph | `81bf17b23` (`langgraph-checkpoint` 4.2.0 package metadata) | Reproduced: `ZoneInfo` becomes fixed-offset `datetime.timezone`, DST +1 day result shifts by one hour, `fold=1` becomes `0` |
| 2026-09-11 | xrwang8/langgraph PR #8882 | `30312c51d3400619b9a10eaa8ce2b2970e915ca7` (`langgraph-checkpoint` 4.2.0 package metadata) | Focused fix verified: `ZoneInfo('America/New_York')` preserved, DST +1 day remains `09:00`, `fold=1` remains `1` |

This fixture pins the original upstream commit for reproduction and records focused external verification of PR #8882. It does not claim a released package contains the fix until upstream merges and publishes it.
