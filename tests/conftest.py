"""Global test configuration and fixtures."""
import pytest
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Automatically enable custom integrations in tests."""
    yield

@pytest.fixture
def mock_handle():
    """Fixture that returns a mocked handle for BatterySlider."""
    mock = MagicMock()
    
    mock._slider_limits = {
        "charge_limit": 0  # Start met een standaard waarde, zoals 0
    }

    return mock