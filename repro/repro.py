import datetime as dt
from zoneinfo import ZoneInfo

from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer


def main() -> None:
    serializer = JsonPlusSerializer(allowed_msgpack_modules=True)
    ny = ZoneInfo("America/New_York")

    before = dt.datetime(2026, 3, 7, 9, 0, tzinfo=ny)
    after = serializer.loads_typed(serializer.dumps_typed(before))

    fold_before = dt.datetime(2026, 11, 1, 1, 30, tzinfo=ny, fold=1)
    fold_after = serializer.loads_typed(serializer.dumps_typed(fold_before))

    print(f"before_tz={before.tzinfo!r}")
    print(f"after_tz={after.tzinfo!r}")
    print(f"equal={before == after}")
    print(f"before_plus1={(before + dt.timedelta(days=1)).astimezone(ny)}")
    print(f"after_plus1={(after + dt.timedelta(days=1)).astimezone(ny)}")
    print(f"fold={fold_before.fold}->{fold_after.fold}")

    zoneinfo_lost = isinstance(before.tzinfo, ZoneInfo) and not isinstance(after.tzinfo, ZoneInfo)
    dst_shifted = (before + dt.timedelta(days=1)).astimezone(ny) != (
        after + dt.timedelta(days=1)
    ).astimezone(ny)
    fold_lost = fold_before.fold != fold_after.fold

    if not (zoneinfo_lost and dst_shifted and fold_lost):
        raise SystemExit("Expected LangGraph checkpoint datetime round-trip bug did not reproduce")

    print("REPRODUCED")


if __name__ == "__main__":
    main()
