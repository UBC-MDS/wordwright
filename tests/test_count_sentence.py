import pytest
from wordwright.count_sentences import count_sentences 

def test_empty_string():
    """
    Test that an empty string returns a sentence count of 0.
    """
    text = ""
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentences counted incorrectly"

def test_no_punctuation_input():
    """
    Test that a string with no punctuation marks returns a sentence count of 0.
    """
    text = "xcxccfssgjkvvhjmbh"
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentences counted incorrectly"

def test_invalid_punctuation_input():
    """
    Test that passing a non-list punctuation argument returns False.
    """
    with pytest.raises(TypeError):
        count_sentences("Hello world! It's a beautiful day? Yes, it is.", "!")
        

def test_multiple_sentence_endings():
    """
    Test that the function counts sentences correctly with multiple sentence endings.
    """
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = [".", "?", "!"]
    assert count_sentences(text, punctuation) == 3, "Sentences counted incorrectly"

def test_multiple_occurrences():
    """
     Test that the function counts multiple occurrences of punctuation marks as separate sentences.
    """
    text = "Exciting!!! Really exciting!!! Isn't it?"
    punctuation = ["?", "!"]
    assert count_sentences(text, punctuation) == 7, "Sentences counted incorrectly"