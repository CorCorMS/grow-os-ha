#!/usr/bin/env python3
# GROW OS HA v4.1 - Loads advisory Plant Buddy profiles from JSON persistence.

import json
from datetime import datetime, timezone

REGISTRY_PATH = "/config/packages/grow_os_ha/grow_os_ha_registry.json"
PROFILES_PATH = "/config/packages/grow_os_ha/grow_os_ha_plant_profiles.json"
DEFAULT_PROFILE = "universal_indoor"


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def flatten_profile(prefix, profile_id, profile_data):
    return {
        f"{prefix}_profile_id": profile_id,
        f"{prefix}_profile_label": profile_data["label"],
        f"{prefix}_temperature_min": profile_data["temperature_min"],
        f"{prefix}_temperature_max": profile_data["temperature_max"],
        f"{prefix}_humidity_min": profile_data["humidity_min"],
        f"{prefix}_humidity_max": profile_data["humidity_max"],
        f"{prefix}_soil_min": profile_data["soil_min"],
        f"{prefix}_soil_max": profile_data["soil_max"],
        f"{prefix}_light_hours_min": profile_data["light_hours_min"],
        f"{prefix}_light_hours_max": profile_data["light_hours_max"],
    }


registry = load_json(REGISTRY_PATH)
profiles = load_json(PROFILES_PATH)["profiles"]

plant1_id = registry.get("plant1_profile", DEFAULT_PROFILE)
plant2_id = registry.get("plant2_profile", DEFAULT_PROFILE)
plant1 = profiles.get(plant1_id, profiles[DEFAULT_PROFILE])
plant2 = profiles.get(plant2_id, profiles[DEFAULT_PROFILE])

payload = {
    "state": "ready",
    "updated_at": datetime.now(timezone.utc).isoformat(),
    **flatten_profile("plant_1", plant1_id, plant1),
    **flatten_profile("plant_2", plant2_id, plant2),
}

print(json.dumps(payload, ensure_ascii=False))



