# GROW OS HA v4.0 Architecture

## Core principle

GROW OS HA v4.0 uses a strict single-source architecture.

- The Arbiter is the only component that makes runtime control decisions.
- Registers define policy and mapping state.
- Mirrors expose values for UI, diagnostics and energy views.
- Actuator automations only execute Arbiter commands.
- Plant Buddy is advisory only.

## Main modules

### Inputs

[packages/grow/grow_inputs.yaml](packages/grow/grow_inputs.yaml)

Contains editable helpers:

- locks
- cycle start
- energy price
- device selectors
- confirmed assignment mirrors
- plant profile selectors

### Registers

[packages/grow/grow_registry.yaml](packages/grow/grow_registry.yaml)

Provides:

- fused temperature and humidity
- current phase
- device registry
- phase policy registry

### Arbiter

[packages/grow/grow_arbiter.yaml](packages/grow/grow_arbiter.yaml)

Evaluates:

- live environment
- phase policy
- operator locks
- tank status
- lighting schedule

Outputs:

- heat command
- ventilation command
- pump commands
- light command
- derived power and energy context

### Actuators

[packages/grow/grow_actuators.yaml](packages/grow/grow_actuators.yaml)

Contains execution-only automations. No policy logic lives here.

### Mirrors

[packages/grow/grow_mirrors.yaml](packages/grow/grow_mirrors.yaml)

Read-only debug and dashboard values derived from the Arbiter and policy register.

### Device mapping persistence

[packages/grow/grow_device_mapping.yaml](packages/grow/grow_device_mapping.yaml)

Lets the UI assign devices and sensors, then writes the confirmed mapping into JSON-backed registers.

### Plant Buddy

- [packages/grow/grow_plant_buddy.yaml](packages/grow/grow_plant_buddy.yaml)
- [packages/grow/grow_plant_buddy_trends.yaml](packages/grow/grow_plant_buddy_trends.yaml)

Provides:

- stress scoring per plant
- advisory climate trend review
- weighted soil reviews
- persistent advisory snapshot

## Installation model

The repository includes a Home Assistant OS installer add-on:

- [grow_os_ha_installer](grow_os_ha_installer)

It copies the v4 payload into `/config` and provides a configuration snippet for merging into an existing installation.

