import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.battery_sim.const import DOMAIN


@pytest.mark.asyncio
async def test_async_setup_entry(hass):
    """Test setting up the battery_sim integration."""

    # Maak een nep config entry aan
    config_entry = MockConfigEntry(
        domain=DOMAIN,
        title="Battery Sim Test",
        data={"name": "TestBattery"},
        unique_id="test_battery_id",
    )

    # Voeg deze toe aan Home Assistant
    config_entry.add_to_hass(hass)

    # Roep setup aan
    assert await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    # Controleer of de integratie correct in hass.data staat
    assert DOMAIN in hass.data
    assert config_entry.entry_id in hass.data[DOMAIN]
