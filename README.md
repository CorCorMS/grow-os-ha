# GROW OS HA v4.0

Single-source grow control for Home Assistant with an Arbiter-first architecture.

This repository contains the current v4.0 state of the Grow Box project:

- one Arbiter as the only decision maker
- policy and device registers as the single source of truth
- mirror-only dashboards and debug sensors
- Plant Buddy advisory logic with trend review and stress scoring
- a Home Assistant OS installer add-on for copying the v4 files into `/config`

## Repository layout

- [configuration.yaml](configuration.yaml) — current HA entry-point example
- [packages/grow](packages/grow) — v4.0 package files
- [lovelace/grow_dashboard.yaml](lovelace/grow_dashboard.yaml) — dashboard v4
- [esphome/grow.v4.example.yaml](esphome/grow.v4.example.yaml) — sanitized ESPHome example
- [grow_os_ha_installer](grow_os_ha_installer) — HAOS installer add-on

## HAOS installation flow

1. Push this repository to GitHub.
2. In Home Assistant, open Settings → Add-ons → Add-on Store → Repositories.
3. Add the GitHub repository URL.
4. Install `Grow OS HA v4 Installer`.
5. Start the installer once.
6. Check your configuration.
7. Restart Home Assistant.

The installer copies:

- `packages/grow/*`
- `lovelace/grow_dashboard.yaml`
- `docs/configuration_snippet.yaml` as a merge helper into `/config`
- an ESPHome example file if enabled in the installer options

## Important note about `configuration.yaml`

The installer does not blindly rewrite an unknown user configuration.

Instead it ships a ready-to-merge snippet:

- [docs/configuration_snippet.yaml](docs/configuration_snippet.yaml)

If your Home Assistant already contains the required package and dashboard blocks, no extra change is needed.

## v4.0 architecture rules

- The Arbiter is the only component that makes control decisions.
- Registers define policy and assignments.
- Mirrors only expose values for UI and diagnostics.
- Automations listen to Arbiter output and do not implement policy logic.
- Plant Buddy is advisory only.

## Git safety

The repository ignores:

- private SSH keys
- runtime Plant Buddy snapshot state
- the live ESPHome node file with local secrets

Use the example ESPHome file as the Git-safe starting point.
