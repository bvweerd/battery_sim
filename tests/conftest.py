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
    class DummyHandle:
        def __init__(self):
            self._name = "TestBattery"
            self._battery_size = 10
            self._charge_limit = 5
            self._charge_state = 5
    return DummyHandle()

