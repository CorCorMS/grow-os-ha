# GROW OS HA v4.1

Arbiter-first grow automation for Home Assistant with a strict single-source-of-truth architecture.

GROW OS HA v4.1 is built around one central idea:

- one Arbiter makes all control decisions
- registers hold policy and device assignments
- mirrors feed dashboards and diagnostics
- actuator automations only execute Arbiter output
- Plant Buddy gives advice, but never controls hardware

## What you get

- Home Assistant package-based grow control
- energy-style YAML dashboard for daily operation
- device and sensor mapping from inside Home Assistant
- Plant Buddy stress scoring and recommendations
- energy, cost and power visibility
- JSON persistence for manual safety locks across restarts
- Home Assistant OS installer add-on for easy deployment

## Live v4.1 status

- Grow OS HA is running on the active v4.1 live structure in Home Assistant OS
- active package path: `packages/grow_os_ha`
- active dashboard path: `lovelace/grow_os_ha_dashboard.yaml`
- dashboard id: `grow-os-ha`
- Home Assistant configuration check passed
- dashboard entities and project references were verified against the live HA registry
- Grow-specific unit and statistics issues were cleaned up
- manual safety locks are now persisted in JSON and restored after restart
- final Grow-only debug finished without relevant open Grow errors

## Quick install on Home Assistant OS

1. Open Home Assistant.
2. Go to Settings -> Add-ons -> Add-on Store.
3. Add this repository under Repositories:
   - `https://github.com/CorCorMS/grow-os-ha`
4. Install `Grow OS HA Installer`.
5. Start the installer once.
6. Merge the generated snippet into your `configuration.yaml` if needed.
7. Run a configuration check.
8. Restart Home Assistant.

The installer copies:

- `packages/grow_os_ha/*`
- `lovelace/grow_os_ha_dashboard.yaml`
- a configuration merge snippet into `/config`
- an optional sanitized ESPHome example

## Manual install

Copy these into your Home Assistant `/config` directory:

- [packages/grow_os_ha](packages/grow_os_ha)
- [lovelace/grow_os_ha_dashboard.yaml](lovelace/grow_os_ha_dashboard.yaml)

Then merge:

- [docs/grow_os_ha_configuration_snippet.yaml](docs/grow_os_ha_configuration_snippet.yaml)

into your existing `configuration.yaml`.

## Repository structure

- [packages/grow_os_ha](packages/grow_os_ha) - the current v4.1 runtime packages
- [lovelace/grow_os_ha_dashboard.yaml](lovelace/grow_os_ha_dashboard.yaml) - dashboard v4.1
- [grow_os_ha_installer](grow_os_ha_installer) - HAOS installer add-on
- [ARCHITECTURE.md](ARCHITECTURE.md) - system design
- [INSTALLATION.md](INSTALLATION.md) - installation details
- [CHANGELOG.md](CHANGELOG.md) - version history

## Architecture in one glance

### Arbiter

The Arbiter is the only place where environmental values, phase policy, tank state and locks become real switching decisions.

### Registers

Registers store:

- device assignments
- sensor assignments
- cycle timing
- phase policy values
- confirmed plant profiles
- persisted manual safety lock state

### Mirrors

Mirrors expose Arbiter and policy values for:

- dashboard sections
- debug views
- energy overview
- diagnostics

### Plant Buddy

Plant Buddy is advisory only. It evaluates:

- temperature
- humidity
- light exposure
- weighted soil moisture per plant

and then publishes stress levels plus recommendations.

## Safe for GitHub

This repository is prepared so that local secrets and runtime state do not belong in Git:

- private SSH keys are ignored
- live ESPHome device config is ignored
- runtime Plant Buddy snapshot state is ignored

Use the safe example here:

- [esphome/grow_os_ha.example.yaml](esphome/grow_os_ha.example.yaml)

## License

This project is not open source.

It is licensed for private personal use only. Use by companies, organizations,
clubs, associations, communities, public institutions, commercial operators, or
other group-based entities is not permitted without prior written permission.

This restriction applies to all repository parts, including code, dashboards,
automations, configuration, JSON data, installer files, and the control logic
itself.

See [LICENSE](LICENSE).

## Version

Current public release target:

- `v4.1.0`
