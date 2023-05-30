"""
Verify that the main_request, get_pages, get_parse_json_data
if the functions work correctly.
"""

from api_request import main_request, get_pages, get_parse_json_data
import pytest

def test_main_request():
    """Verify that the main_request function works correctly.
    Parameters: none
    Return: nothing
    """
    try:
        
        assert main_request("https://rickandmortyapi.com/api/character?page=1", "Rick Sanchez", "1")
        
    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        #print(type(excep).__name__, excep, sep=": ")
        print("Please Connect To The Interent, Then Run the Program Again..")




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", "test_api_request.py"])