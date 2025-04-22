"""Test the BatterySlider number entity."""

import pytest
from custom_components.battery_sim.number import BatterySlider
from custom_components.battery_sim.const import CHARGE_LIMIT
from homeassistant.components.number import NumberMode

from tests.conftest import mock_handle


@pytest.mark.asyncio
async def test_battery_slider_initialization(mock_handle):
    """Test that the BatterySlider initializes correctly."""
    slider = BatterySlider(mock_handle, CHARGE_LIMIT, "charge_limit", "mdi:battery")
    assert slider.name == "TestBattery - charge_limit"
    

@pytest.mark.asyncio
async def test_battery_slider_set_value(hass):
    """Test setting a new value on the BatterySlider."""

    handle = mock_handle("TestBattery")
    slider = BatterySlider(handle, CHARGE_LIMIT, "charge_limit", "mdi:battery")

    await slider.async_set_native_value(2.5)

    assert slider.native_value == 2.5
    assert handle._slider_limits["charge_limit"] == 2.5
