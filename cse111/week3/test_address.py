"""
Verify that the extract_city, extract_state,
and extract_zipcode functions work correctly.
"""

from address import extract_city, \
    extract_state, extract_zipcode
import pytest


def test_extract_city():
    """Verify that the extract city function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"

def test_extract_state():
    """Verify that the extract state function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    
def test_extract_zipcode():
    """Verify that the extract zipcode function works correctly.
    Parameters: none
    Return: nothing
    """
    
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", "test_address.py"])