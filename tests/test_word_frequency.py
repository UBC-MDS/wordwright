from wordwright.word_frequency import frequent_words
import pytest
from collections import Counter

def test_frequent_words_non_string_input():
    """
    Test frequent_words with non-string text input.
    
    This test ensures that the frequent_words function raises a TypeError 
    when the text input is not a string. Various non-string types are tested 
    including integers, floats, and boolean values.
    """
    with pytest.raises(TypeError):
        frequent_words(123)
    with pytest.raises(TypeError):
        frequent_words(123.123)
    with pytest.raises(TypeError):
        frequent_words(False)

def test_frequent_words_non_list_stopwords():
    """
    Test frequent_words with non-list stopwords input.
    
    This test verifies that the function raises a TypeError when the stopwords 
    argument is not a list. It tests different non-list types including strings, 
    boolean values, and integers.
    """
    with pytest.raises(TypeError):
        frequent_words("Some text", "not a list")
    with pytest.raises(TypeError):
        frequent_words("Some text", False)
    with pytest.raises(TypeError):
        frequent_words("Some text", 123)

def test_frequent_words_non_string_in_stopwords():
    """
    Test frequent_words with non-string elements in the stopwords list.
    
    This test checks that the function raises a TypeError if the stopwords list 
    contains non-string elements. It tests various types like integers, 
    boolean values, and dictionaries.
    """
    with pytest.raises(TypeError):
        frequent_words("Some text", [1, 2, 3])
    with pytest.raises(TypeError):
        frequent_words("Some text", [True, False])
    with pytest.raises(TypeError):
        frequent_words("Some text", [{"apple": 1}])

def test_frequent_words_standard_input():
    """
    Test frequent_words with standard text input.
    
    This test checks if the frequent_words function correctly counts and returns 
    the frequency of each word in a given text. A sample text is used to verify 
    that the function returns the expected word count.
    """
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    expected = Counter({'the': 3, 'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 
                        'over': 1, 'lazy': 1, 'dog': 1, 'was': 1, 'very': 1})
    assert frequent_words(text) == expected, "Failed with standard input"

def test_frequent_words_with_stopwords():
    """
    Test frequent_words functionality with stopwords.
    
    This test verifies that the function correctly excludes specified stopwords 
    from the word count. It uses a sample text and a list of stopwords to ensure 
    that the word count returned does not include these stopwords.
    """
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    stopwords = ["the", "over", "was", "very"]
    expected = Counter({'quick': 2, 'fox': 2, 'brown': 1, 
                        'jumps': 1, 'lazy': 1, 'dog': 1})
    assert frequent_words(text, stopwords) == expected, "Failed with stopwords"

def test_frequent_words_empty_text():
    """
    Test frequent_words with empty text input.
    
    This test ensures that the frequent_words function correctly handles an 
    empty string input, returning an empty Counter object without any errors.
    """
    assert frequent_words("") == Counter(), "Failed with empty text"
