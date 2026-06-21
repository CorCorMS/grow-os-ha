#!/usr/bin/env python3
###############################################################################
# GROW OS HA v4.1 - LOCK STATE LOADER
# Loads persisted manual safety locks from JSON so HA can restore operator
# safety overrides after restart without reintroducing policy logic elsewhere.
###############################################################################

from __future__ import annotations

import json
from pathlib import Path

PATH = Path("/config/packages/grow_os_ha/grow_os_ha_lock_state.json")

DEFAULT = {
    "state": "ready",
    "updated_at": "1970-01-01T00:00:00+00:00",
    "master_lock": False,
    "heating_lock": False,
    "ventilation_lock": False,
    "irrigation_lock": False,
    "lighting_lock": False,
}


def main() -> None:
    payload = DEFAULT.copy()
    if PATH.exists():
        try:
            raw = json.loads(PATH.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                payload.update({k: raw.get(k, v) for k, v in DEFAULT.items() if k != "state"})
        except Exception:
            payload["state"] = "error"
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()
