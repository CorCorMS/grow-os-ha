# GROW OS HA v4.1 Installation

## Option 1: Home Assistant OS repository install

1. Push this repository to GitHub.
2. Open Home Assistant.
3. Go to Settings -> Add-ons -> Add-on Store -> Repositories.
4. Add the GitHub repository URL.
5. Install `Grow OS HA Installer`.
6. Start the add-on once.
7. Merge `/config/grow_os_ha_configuration_snippet.yaml` into your `configuration.yaml` if needed.
8. Run a configuration check.
9. Restart Home Assistant.

## Option 2: Manual install

Copy these folders into `/config`:

- `packages/grow_os_ha`
- `lovelace/grow_os_ha_dashboard.yaml`

Then merge:

- [docs/grow_os_ha_configuration_snippet.yaml](docs/grow_os_ha_configuration_snippet.yaml)

into your Home Assistant configuration.

## Optional ESPHome

Use:

- [esphome/grow_os_ha.example.yaml](esphome/grow_os_ha.example.yaml)

as the safe starting point. Do not commit your live ESPHome secrets.

## Current live target

The current v4.1 live target is:

- package path `packages/grow_os_ha`
- dashboard path `lovelace/grow_os_ha_dashboard.yaml`
- dashboard id `grow-os-ha`
