#!/usr/bin/env python3
###############################################################################
# GROW OS HA v4.1 - LOCK STATE WRITER
# Persists the manual Grow safety locks to JSON so operator overrides survive
# Home Assistant restarts and remain separate from Arbiter policy logic.
###############################################################################

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

PATH = Path("/config/packages/grow_os_ha/grow_os_ha_lock_state.json")
FILE_MODE = 0o644
DEFAULT = {
    "updated_at": "1970-01-01T00:00:00+00:00",
    "master_lock": False,
    "heating_lock": False,
    "ventilation_lock": False,
    "irrigation_lock": False,
    "lighting_lock": False,
}


def atomic_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=path.parent, encoding="utf-8") as tmp:
        json.dump(payload, tmp, ensure_ascii=False, indent=2)
        tmp.write("\n")
        tmp_path = Path(tmp.name)
    os.chmod(tmp_path, FILE_MODE)
    os.replace(tmp_path, path)
    os.chmod(path, FILE_MODE)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: grow_os_ha_lock_state_writer.py '<json>'")
    incoming = json.loads(sys.argv[1])
    payload = DEFAULT.copy()
    if PATH.exists():
        try:
            current = json.loads(PATH.read_text(encoding="utf-8"))
            if isinstance(current, dict):
                payload.update(current)
        except Exception:
            pass
    payload.update(
        {
            "updated_at": incoming.get("updated_at", payload["updated_at"]),
            "master_lock": bool(incoming.get("master_lock", payload["master_lock"])),
            "heating_lock": bool(incoming.get("heating_lock", payload["heating_lock"])),
            "ventilation_lock": bool(incoming.get("ventilation_lock", payload["ventilation_lock"])),
            "irrigation_lock": bool(incoming.get("irrigation_lock", payload["irrigation_lock"])),
            "lighting_lock": bool(incoming.get("lighting_lock", payload["lighting_lock"])),
        }
    )
    atomic_write(PATH, payload)


if __name__ == "__main__":
    main()
