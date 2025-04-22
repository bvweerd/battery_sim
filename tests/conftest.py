"""Fixtures for testing."""

import pytest

class DummyHandle:
    def __init__(self, name):
        self._name = name
        self._max_charge_rate = 3.5
        self._max_discharge_rate = 4.0
        self._slider_limits = {}

    def set_slider_limit(self, value, key):
        self._slider_limits[key] = value


@pytest.fixture
def mock_handle():
    def _make(name="TestBattery"):
        return DummyHandle(name)
    return _make

#@pytest.fixture(autouse=True)
#def auto_enable_custom_integrations(enable_custom_integrations):
#    """Enable custom integrations."""
#    return
