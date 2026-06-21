#!/usr/bin/with-contenv bashio
# GROW OS HA v4.1 - HAOS installer add-on.
# Copies the repository payload into /config without trying to guess every
# detail of a foreign configuration.yaml structure.

set -euo pipefail

CONFIG_DIR="/homeassistant"
PAYLOAD_DIR="/payload"
BACKUP_DIR="${CONFIG_DIR}/grow_os_ha_v4_1_backups/$(date +%Y%m%d-%H%M%S)"

OVERWRITE="$(bashio::config 'overwrite_existing')"
CREATE_BACKUP="$(bashio::config 'create_backup')"
INSTALL_ESPHOME="$(bashio::config 'install_example_esphome')"

copy_file() {
    local source="$1"
    local target="$2"

    mkdir -p "$(dirname "${target}")"

    if bashio::var.true "${CREATE_BACKUP}" && [ -f "${target}" ]; then
        mkdir -p "${BACKUP_DIR}/$(dirname "${target#${CONFIG_DIR}/}")"
        cp -f "${target}" "${BACKUP_DIR}/${target#${CONFIG_DIR}/}"
    fi

    if [ -f "${target}" ] && ! bashio::var.true "${OVERWRITE}"; then
        bashio::log.info "Skip existing file: ${target}"
        return 0
    fi

    cp -f "${source}" "${target}"
    bashio::log.info "Installed: ${target}"
}

bashio::log.info "Installing Grow OS HA v4.1 payload..."

mkdir -p "${CONFIG_DIR}/packages/grow_os_ha" "${CONFIG_DIR}/lovelace"

for file in "${PAYLOAD_DIR}"/packages/grow_os_ha/*; do
    copy_file "${file}" "${CONFIG_DIR}/packages/grow_os_ha/$(basename "${file}")"
done

copy_file "${PAYLOAD_DIR}/lovelace/grow_os_ha_dashboard.yaml" "${CONFIG_DIR}/lovelace/grow_os_ha_dashboard.yaml"
copy_file "${PAYLOAD_DIR}/examples/grow_os_ha_configuration_snippet.yaml" "${CONFIG_DIR}/grow_os_ha_configuration_snippet.yaml"

if bashio::var.true "${INSTALL_ESPHOME}"; then
    mkdir -p "${CONFIG_DIR}/esphome"
    copy_file "${PAYLOAD_DIR}/examples/grow_os_ha.example.yaml" "${CONFIG_DIR}/esphome/grow_os_ha.example.yaml"
fi

if grep -q "packages/grow_os_ha" "${CONFIG_DIR}/configuration.yaml" 2>/dev/null; then
    bashio::log.info "configuration.yaml already references packages/grow_os_ha."
else
    bashio::log.warning "configuration.yaml does not yet reference packages/grow_os_ha."
    bashio::log.warning "Merge /config/grow_os_ha_configuration_snippet.yaml into /config/configuration.yaml."
fi

if grep -q "lovelace/grow_os_ha_dashboard.yaml" "${CONFIG_DIR}/configuration.yaml" 2>/dev/null; then
    bashio::log.info "configuration.yaml already references the Grow dashboard."
else
    bashio::log.warning "Dashboard entry not detected in configuration.yaml."
    bashio::log.warning "Merge /config/grow_os_ha_configuration_snippet.yaml into /config/configuration.yaml."
fi

bashio::log.info "Grow OS HA v4.1 installer finished."
bashio::log.info "Next step: run Home Assistant configuration check, then restart Home Assistant."



