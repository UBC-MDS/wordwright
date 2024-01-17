from wordwright.word_frequency import frequent_words
import pytest
from collections import Counter

def test_frequent_words_non_string_input():
    with pytest.raises(TypeError):
        frequent_words(123)
    with pytest.raises(TypeError):
        frequent_words(123.123)
    with pytest.raises(TypeError):
        frequent_words(False)

def test_frequent_words_non_list_stopwords():
    with pytest.raises(TypeError):
        frequent_words("Some text", "not a list")
    with pytest.raises(TypeError):
        frequent_words("Some text", False)
    with pytest.raises(TypeError):
        frequent_words("Some text", 123)

def test_frequent_words_non_string_in_stopwords():
    with pytest.raises(TypeError):
        frequent_words("Some text", [1, 2, 3])
    with pytest.raises(TypeError):
        frequent_words("Some text", [True, False])
    with pytest.raises(TypeError):
        frequent_words("Some text", [{"apple": 1}])

def test_frequent_words_standard_input():
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    expected = Counter({'the': 3, 'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 
                        'over': 1, 'lazy': 1, 'dog': 1, 'was': 1, 'very': 1})
    assert frequent_words(text) == expected, "Failed with standard input"

def test_frequent_words_with_stopwords():
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    stopwords = ["the", "over", "was", "very"]
    expected = Counter({'quick': 2, 'fox': 2, 'brown': 1, 
                        'jumps': 1, 'lazy': 1, 'dog': 1})
    assert frequent_words(text, stopwords) == expected, "Failed with stopwords"

def test_frequent_words_empty_text():
    assert frequent_words("") == Counter(), "Failed with empty text"
