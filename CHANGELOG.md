# Changelog

## v4.1.0

- manual safety locks are now persisted in JSON
- manual safety locks are restored automatically after Home Assistant restarts
- lock restore timing was hardened for early startup phases
- lock persistence was added to the installer payload
- repository documentation, installer texts and runtime headers were aligned to v4.1

## v4.0.0

- Arbiter-first architecture finalized
- single-source policy and device registry approach
- actuator automations reduced to execution-only mirrors
- v4 dashboard prepared for Home Assistant YAML mode
- Plant Buddy advisory system added
- climate and soil trend reviews added
- energy and cost overview aligned with cabinet and Shelly measurements
- legacy restored/unavailable Grow entities cleaned out of Home Assistant
- HAOS installer add-on added to repository
- live Home Assistant structure migrated to `grow_os_ha`
- final dashboard path migrated to `lovelace/grow_os_ha_dashboard.yaml`
- dashboard, package references and live entity mapping verified
- Grow-specific temperature unit/statistics issue cleaned up
