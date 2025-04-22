"""Fixtures for testing."""

import pytest

@pytest.fixture
def mock_handle():
    class DummyHandle:
        def __init__(self):
            self._name = "TestBattery"
            self._battery_size = 10
            self._charge_limit = 5
            self._charge_state = 5
    return DummyHandle()

