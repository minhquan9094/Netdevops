# filename: test_mac_address.py 
# code to improve use case with assert and test multiple mac address from dict

import pytest
from mac_address import normalize_mac_address # parse mac address function


#### Function to get mac address

@pytest.fixture
def non_normalized_mac_list():
    return ["aabb.ccdd.eeff", "0011.2233.4455", "aa11.bb22.cc33"]

@pytest.fixture()
def normalized_mac_list():
    return [
        "aa:bb:cc:dd:ee:ff", 
        "00:11:22:33:44:55", 
        "aa:11:bb:22:cc:33"
        ]

def test_normalize_mac_address_lists(non_normalized_mac_list, normalized_mac_list):
    for sequence, mac_address in enumerate(non_normalized_mac_list):
        assert normalize_mac_address(mac_address) == normalized_mac_list[sequence],f"{mac_address} - FAILED"

