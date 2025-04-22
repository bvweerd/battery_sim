import pytest
from unittest.mock import patch

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntryState
from homeassistant.setup import async_setup_component

from custom_components.battery_sim.const import DOMAIN

from pytest_homeassistant_custom_component.common import MockConfigEntry

pytestmark = pytest.mark.asyncio

async def test_async_setup_entry(hass: HomeAssistant) -> None:
    """Test setting up and unloading the integration."""
    mock_entry = MockConfigEntry(
        domain=DOMAIN,
        data={},
        entry_id="test_entry_id"
    )
    mock_entry.add_to_hass(hass)

    with patch(
        "custom_components.battery_sim.async_setup_entry", return_value=True
    ) as mock_setup_entry:
        assert await async_setup_component(hass, DOMAIN, {}) is True
        await hass.async_block_till_done()

        assert mock_setup_entry.called

async def test_async_setup_entry_and_unload(hass: HomeAssistant) -> None:
    """Test integration is setup and can be unloaded."""
    mock_entry = MockConfigEntry(
        domain=DOMAIN,
        data={},
        entry_id="test_entry_id"
    )
    mock_entry.add_to_hass(hass)

    with patch("custom_components.battery_sim.number.async_setup_entry", return_value=True):
        from custom_components.battery_sim import async_setup_entry, async_unload_entry

        # Setup the entry
        assert await async_setup_entry(hass, mock_entry) is True
        assert mock_entry.state == ConfigEntryState.LOADED

        # Unload the entry
        assert await async_unload_entry(hass, mock_entry) is True
        assert mock_entry.state == ConfigEntryState.NOT_LOADED
