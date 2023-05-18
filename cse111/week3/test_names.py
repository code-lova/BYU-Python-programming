"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make full name function works correctly.
    Parameters: none
    Return: nothing
    """
    
    assert make_full_name("Jerry", "Ebizo-Joseph") == "Ebizo-Joseph;Jerry"
    assert make_full_name("Matthew", "Rufford") == "Rufford;Matthew"
    assert make_full_name("B", "Cl") == "Cl;B"
    assert make_full_name("", "") == ";"


def test_extract_family_name():
    """Verify that the extract family name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("Ebizo-Joseph; Jerry") == "Ebizo-Joseph"
    assert extract_family_name("Rufford; Matthew") == "Rufford"
    assert extract_family_name("Cl; B") == "Cl"
    assert extract_family_name("; ") == ""
    
    
def test_extract_given_name():
    """Verify that the extract given name function works correctly.
    Parameters: none
    Return: nothing
    """
    
    assert extract_given_name("Ebizo-Joseph; Jerry") == "Jerry"
    assert extract_given_name("Rufford; Matthew") == "Matthew"
    assert extract_given_name("Cl; B") == "B"
    assert extract_given_name("; ") == ""
    
    
     
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])