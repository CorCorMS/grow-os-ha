#!/usr/bin/env python3
# GROW v4.0 — Atomic JSON persistence for dashboard device assignments.

import json
import os
import re
import sys
import tempfile

PATH = "/config/packages/grow/grow_registry.json"
ROLES = {"light", "heat", "vent", "pump1", "pump2", "temperature", "humidity", "soil1", "soil2", "tank"}
ENTITY_ID = re.compile(r"^(?:light|switch|sensor)\.[a-z0-9_]+$")

role, entity_id = sys.argv[1:]
if role not in ROLES or not ENTITY_ID.fullmatch(entity_id):
    raise SystemExit("Invalid Grow v4 device mapping")
with open(PATH, encoding="utf-8") as source:
    data = json.load(source)
data[role] = entity_id
with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=os.path.dirname(PATH), delete=False) as target:
    json.dump(data, target, indent=2, ensure_ascii=False)
    target.write("\n")
    temporary = target.name
os.replace(temporary, PATH)
