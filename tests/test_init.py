import pytest
from custom_components.battery_sim.const import DOMAIN

from homeassistant.config_entries import ConfigEntryState

from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.helpers.entity_component import async_update_entity
from homeassistant.helpers import entity_platform

from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.const import CONF_NAME

from pytest_homeassistant_custom_component.common import MockConfigEntry

@pytest.mark.asyncio
async def test_async_setup_entry(hass):
    """Test setting up the integration."""

    config_entry = MockConfigEntry(
        domain=DOMAIN,
        title="Battery Sim Test",
        data={"name": "TestBattery"},
        unique_id="test_battery_id"
    )
    config_entry.add_to_hass(hass)

    # Setup the entry
    assert await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    # Verify that the integration data is set
    assert DOMAIN in hass.data
    assert config_entry.entry_id in hass.data[DOMAIN]
    assert config_entry.state == ConfigEntryState.LOADED
