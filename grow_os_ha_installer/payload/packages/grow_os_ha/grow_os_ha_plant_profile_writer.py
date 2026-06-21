#!/usr/bin/env python3
# GROW OS HA v4.1 - Atomic JSON persistence for confirmed Plant Buddy profiles.

import json
import os
import re
import sys
import tempfile

PATH = "/config/packages/grow_os_ha/grow_os_ha_registry.json"
ROLES = {"plant1_profile", "plant2_profile"}
PROFILE = re.compile(r"^[a-z0-9_]+$")

role, profile_name = sys.argv[1:]
if role not in ROLES or not PROFILE.fullmatch(profile_name):
    raise SystemExit("Invalid Grow v4 plant profile mapping")

with open(PATH, encoding="utf-8") as source:
    data = json.load(source)

data[role] = profile_name

with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=os.path.dirname(PATH), delete=False) as target:
    json.dump(data, target, indent=2, ensure_ascii=False)
    target.write("\n")
    temporary = target.name

os.replace(temporary, PATH)



