# filename: test_mac_address.py 
import pytest
from mac_address import normalize_mac_address

def test_normalize_mac_address(non_normalized_mac_address, expected_mac_address):
    normalized_mac_address = normalize_mac_address(non_normalized_mac_address)
    assert normalized_mac_address == expected_mac_address

@pytest.fixture
def non_normalized_mac_address():
    return "aabb.ccdd.eaff"
    #return "aa:bb:cc:dd:ee:ff"

@pytest.fixture
def expected_mac_address():
    return "aa:bb:cc:dd:ee:ff"