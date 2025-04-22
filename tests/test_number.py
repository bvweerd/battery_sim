"""Test the BatterySlider number entity."""

import pytest
from custom_components.battery_sim.number import BatterySlider
from battery_sim.const import CHARGE_LIMIT
from homeassistant.components.number import NumberMode

from tests.conftest import mock_handle


@pytest.mark.asyncio
async def test_battery_slider_initialization(hass):
    """Test that the BatterySlider initializes correctly."""

    handle = mock_handle("TestBattery")
    slider = BatterySlider(handle, CHARGE_LIMIT, "charge_limit", "mdi:battery")

    assert slider.name == "TestBattery - Charge Limit"
    assert slider.unique_id == "TestBattery - Charge Limit"
    assert slider.native_min_value == 0.00
    assert slider.native_max_value == handle._max_charge_rate
    assert slider.native_step == 0.01
    assert slider.native_value == handle._max_charge_rate
    assert slider.icon == "mdi:battery"
    assert slider.mode == NumberMode.BOX
    assert slider.unit_of_measurement == "kW"


@pytest.mark.asyncio
async def test_battery_slider_set_value(hass):
    """Test setting a new value on the BatterySlider."""

    handle = mock_handle("TestBattery")
    slider = BatterySlider(handle, CHARGE_LIMIT, "charge_limit", "mdi:battery")

    await slider.async_set_native_value(2.5)

    assert slider.native_value == 2.5
    assert handle._slider_limits["charge_limit"] == 2.5
