import datetime as dt
from zoneinfo import ZoneInfo

from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer


def pack(value: dt.datetime) -> dict[str, object]:
    zone_key = getattr(value.tzinfo, "key", None)
    if not zone_key:
        raise ValueError("Expected an IANA ZoneInfo timezone")
    return {"instant": value, "zone": zone_key, "fold": value.fold}


def unpack(payload: dict[str, object]) -> dt.datetime:
    instant = payload["instant"]
    if not isinstance(instant, dt.datetime):
        raise TypeError("Restored payload did not contain a datetime")
    return instant.astimezone(ZoneInfo(str(payload["zone"]))).replace(fold=int(payload["fold"]))


def main() -> None:
    serializer = JsonPlusSerializer(allowed_msgpack_modules=True)
    ny = ZoneInfo("America/New_York")
    before = dt.datetime(2026, 3, 7, 9, 0, tzinfo=ny)

    restored_payload = serializer.loads_typed(serializer.dumps_typed(pack(before)))
    restored = unpack(restored_payload)
    next_day = restored + dt.timedelta(days=1)

    print(f"restored_tz={restored.tzinfo!r}")
    print(f"next_day={next_day}")

    if getattr(restored.tzinfo, "key", None) != "America/New_York":
        raise SystemExit("Containment did not restore the IANA timezone")
    if next_day.isoformat() != "2026-03-08T09:00:00-04:00":
        raise SystemExit("Containment did not preserve DST-aware wall-clock arithmetic")

    print("CONTAINMENT_OK")


if __name__ == "__main__":
    main()
