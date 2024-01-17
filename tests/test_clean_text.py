import pytest
from wordwright.preprocessing import clean_text

def test_clean_text_non_string_input():
    """ 
    Test for correct input data types, 
    e.g., integer, float, boolean
    """
    with pytest.raises(TypeError):
        clean_text(123)
    with pytest.raises(TypeError):
        clean_text(123.123)
    with pytest.raises(TypeError):
        clean_text(True)

def test_clean_text_standard_input():
    """
    Test clean_text with standard text input.
    
    This test checks if clean_text correctly cleans a standard string which 
    includes punctuation, standalone apostrophes, and  a mixed case letters. 
    It verifies that the function converts the string to lowercase and 
    removes all punctuation except apostrophes that directly follow a character.
    """
    assert (clean_text("It's a sunny day. ' ' ,Let's GO!'") == 
            "it's a sunny day let's go"), "Failed to clean text input"

def test_clean_text_empty_string():
    """
    Test clean_text with an empty string input.
    
    This test verifies that clean_text correctly handles an empty string input,
    returning an empty string without raising any errors.
    """
    assert clean_text("") == "", "Failed on empty string input"

def test_clean_text_only_punctuation():
    """
    Test clean_text with a string containing only punctuation.
    
    This test checks if clean_text properly cleans a string that consists solely of
    punctuation characters (apostrophes included). The expected output is an empty string.
    """
    assert (clean_text("!!!, ,,,!!!") == 
            ""), "Failed to clean a string with only punctuation"
    assert (clean_text("!!!, ,,,' ' ' '!!!") == 
            ""), "Failed to clean a string with only punctuation"
