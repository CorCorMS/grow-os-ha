#!/usr/bin/env python3
# GROW OS HA v4.0 - Atomic JSON persistence for Plant Buddy advisory snapshots.

import json
import os
import sys
import tempfile

PATH = "/config/packages/grow_os_ha/grow_os_ha_plant_buddy_snapshot.json"

payload = json.loads(sys.argv[1])

with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=os.path.dirname(PATH), delete=False) as target:
    json.dump(payload, target, indent=2, ensure_ascii=False)
    target.write("\n")
    temporary = target.name

os.replace(temporary, PATH)



