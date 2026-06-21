# GROW OS HA v4.1 Architecture

## Core principle

GROW OS HA v4.1 uses a strict single-source architecture.

- The Arbiter is the only component that makes runtime control decisions.
- Registers define policy and mapping state.
- Mirrors expose values for UI, diagnostics and energy views.
- Actuator automations only execute Arbiter commands.
- Plant Buddy is advisory only.
- Manual safety locks persist in JSON and are restored after restart.

## Main modules

### Inputs

[packages/grow_os_ha/grow_os_ha_inputs.yaml](packages/grow_os_ha/grow_os_ha_inputs.yaml)

Contains editable helpers:

- device and sensor selections
- confirmed mappings
- cycle start
- safety locks
- vent probe state

### Registry

[packages/grow_os_ha/grow_os_ha_registry.yaml](packages/grow_os_ha/grow_os_ha_registry.yaml)

Contains the policy and assignment mirrors consumed by the Arbiter.

### Arbiter

[packages/grow_os_ha/grow_os_ha_arbiter.yaml](packages/grow_os_ha/grow_os_ha_arbiter.yaml)

This is the single source of truth for runtime decisions.

### Actuators

[packages/grow_os_ha/grow_os_ha_actuators.yaml](packages/grow_os_ha/grow_os_ha_actuators.yaml)

Contains execution-only automations that mirror Arbiter commands.

### Plant Buddy

[packages/grow_os_ha/grow_os_ha_plant_buddy.yaml](packages/grow_os_ha/grow_os_ha_plant_buddy.yaml)

Publishes advisory stress levels and recommendations only.

### Dashboard

[lovelace/grow_os_ha_dashboard.yaml](lovelace/grow_os_ha_dashboard.yaml)

Shows the operational UI, energy views, Arbiter status and Plant Buddy summaries.
