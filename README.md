# GROW OS HA v4.0

Arbiter-first grow automation for Home Assistant with a strict single-source-of-truth architecture.

GROW OS HA v4.0 is built around one central idea:

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
- Home Assistant OS installer add-on for easy deployment

## Quick install on Home Assistant OS

1. Open Home Assistant.
2. Go to Settings → Add-ons → Add-on Store.
3. Add this repository under Repositories:
   - `https://github.com/CorCorMS/grow-os-ha`
4. Install `Grow OS HA v4 Installer`.
5. Start the installer once.
6. Merge the generated snippet into your `configuration.yaml` if needed.
7. Run a configuration check.
8. Restart Home Assistant.

The installer copies:

- `packages/grow/*`
- `lovelace/grow_dashboard.yaml`
- a configuration merge snippet into `/config`
- an optional sanitized ESPHome example

## Manual install

Copy these into your Home Assistant `/config` directory:

- [packages/grow](packages/grow)
- [lovelace/grow_dashboard.yaml](lovelace/grow_dashboard.yaml)

Then merge:

- [docs/configuration_snippet.yaml](docs/configuration_snippet.yaml)

into your existing `configuration.yaml`.

## Repository structure

- [packages/grow](packages/grow) — the current v4.0 runtime packages
- [lovelace/grow_dashboard.yaml](lovelace/grow_dashboard.yaml) — dashboard v4
- [grow_os_ha_installer](grow_os_ha_installer) — HAOS installer add-on
- [ARCHITECTURE.md](ARCHITECTURE.md) — system design
- [INSTALLATION.md](INSTALLATION.md) — installation details
- [CHANGELOG.md](CHANGELOG.md) — version history

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

- [esphome/grow.v4.example.yaml](esphome/grow.v4.example.yaml)

## Version

Current public release target:

- `v4.0.0`
