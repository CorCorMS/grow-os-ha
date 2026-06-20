# Grow OS HA v4 Installer

Home Assistant OS add-on that copies the current Grow OS HA v4.0 payload into `/config`.

## What it installs

- `packages/grow_os_ha/*`
- `lovelace/grow_os_ha_dashboard.yaml`
- `grow_os_ha_configuration_snippet.yaml`
- optional `esphome/grow_os_ha.example.yaml`

## What it does not do

- It does not guess or rewrite an unknown user configuration layout.
- It does not change your entity mappings or live registers on its own.

## Typical use

1. Install the add-on from the repository.
2. Start it once.
3. Merge the generated configuration snippet if your config does not yet include the package and dashboard blocks.
4. Check configuration.
5. Restart Home Assistant.


