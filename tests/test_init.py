"""Test the Battery Sim integration initialization."""
import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from homeassistant.core import HomeAssistant

from custom_components.battery_sim.const import (
    DOMAIN,
    CONF_BATTERY_CAPACITY,
    CONF_BATTERY_MAX_CHARGE_RATE,
    CONF_BATTERY_MAX_DISCHARGE_RATE,
    CONF_BATTERY_START_CHARGE,
    CONF_INITIAL_MODE,
    DEFAULT_MODE,
)

@pytest.mark.asyncio
async def test_async_setup_entry(hass: HomeAssistant):
    """Test successful setup of a config entry."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Battery Sim Test",
        data={
            CONF_BATTERY_NAME: "Test Battery",
            CONF_BATTERY_CAPACITY: 10.0,               # kWh
            CONF_BATTERY_MAX_CHARGE_RATE: 2.0,         # kW
            CONF_BATTERY_MAX_DISCHARGE_RATE: 2.0,      # kW
            CONF_BATTERY_START_CHARGE: 50.0,           # %
            CONF_INITIAL_MODE: DEFAULT_MODE,           # e.g. "default"
        },
        unique_id="test_battery_id"
    )
    
    entry.add_to_hass(hass)

    # Setup the config entry
    result = await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert result is True
    assert DOMAIN in hass.data
    assert entry.entry_id in hass.data[DOMAIN]


@pytest.mark.asyncio
async def test_async_unload_entry(hass: HomeAssistant):
    """Test unloading the config entry."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Test Battery Sim",
        data={"name": "TestBattery"},
        unique_id="test_battery_id",
    )
    entry.add_to_hass(hass)

    # Setup and then unload
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.entry_id not in hass.data.get(DOMAIN, {})
