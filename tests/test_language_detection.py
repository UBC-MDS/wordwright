import pytest
from langdetect import LangDetectException
from wordwright.language_detection import language_detection 
from unittest.mock import patch

def test_language_detection_english():
    """
    Test whether the language_detection function correctly identifies English text.
    """
    assert language_detection("This is a sample English text.") == "English"

def test_language_detection_non_english():
    """
    Test whether the language_detection function correctly identifies non-English text.
    """
    assert language_detection("Este es un texto en español.") == "Not English"

def test_language_detection_empty_string():
    """
    Test whether the language_detection function raises a ValueError for empty string input.
    """
    with pytest.raises(ValueError) as excinfo:
        language_detection("")
    assert str(excinfo.value) == "Input string is empty or whitespace."

def test_language_detection_whitespace_string():
    """
    Test whether the language_detection function raises a ValueError for whitespace string input.
    """
    with pytest.raises(ValueError) as excinfo:
        language_detection("   ")
    assert str(excinfo.value) == "Input string is empty or whitespace."

def test_language_detection_non_string_input():
    """
    Test whether the language_detection function raises a ValueError when input is not a string.
    """
    with pytest.raises(ValueError) as excinfo:
        language_detection(123)
    assert str(excinfo.value) == "Input must be a string."

@patch('wordwright.language_detection.detect')
def test_language_detection_detection_exception(mock_detect):
    """
    Test if the function correctly handles a LangDetectException.
    """
    # Set up the mock to raise LangDetectException with the required arguments
    mock_detect.side_effect = LangDetectException(0, "message")

    assert language_detection("Test text") == "Language detection error"
