import pytest
from collections import Counter
from wordwright.count_keywords import count_keywords

def test_count_keywords_non_string_text():
    with pytest.raises(TypeError):
        count_keywords(123, ['123'])
    with pytest.raises(TypeError):
        count_keywords([123], ['123'])
    with pytest.raises(TypeError):
        count_keywords(True, ['123'])

def test_count_keywords_non_list_keywords():
    with pytest.raises(TypeError):
        count_keywords('ab', '123')
    with pytest.raises(TypeError):
        count_keywords('ab', 123)
    with pytest.raises(TypeError):
        count_keywords('ab', True)
    with pytest.raises(TypeError):
        count_keywords('ab', {'cheese': 'sticks'})

def test_count_keywords_non_string_keyword():
    with pytest.raises(TypeError):
        count_keywords('ab', [123])
    with pytest.raises(TypeError):
        count_keywords('ab', [123, '123'])
    with pytest.raises(TypeError):
        count_keywords('ab', ['123', {'cheese': 'sticks'}])
    with pytest.raises(TypeError):
        count_keywords('ab', [[], '123'])
    with pytest.raises(TypeError):
        count_keywords('ab', [['123'], '123'])
    with pytest.raises(TypeError):
        count_keywords('ab', [True, '123'])
    with pytest.raises(TypeError):
        count_keywords('ab', ['True', 123])

def test_count_keywords_correct_output():
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    keywords = ['the', 'dog', 'quick']
    expected = Counter({'the': 3, 'dog': 1, 'quick': 2})
    assert count_keywords(text, keywords) == expected, "Incorrect output!"

def test_count_keywords_correct_keyword_order():
    text = "alpha bravo charlie delta"
    keywords = ['delta', 'charlie', 'bravo', 'alpha']
    expected = Counter({'delta': 1, 'charlie': 1, 'bravo': 1, 'alpha': 1})
    assert count_keywords(text, keywords) == expected, "Incorrect keyword order!"

def test_count_keywords_unique_keyword_output():
    text = "who are you with?"
    keywords = ['you!', 'who', 'You', 'you', 
                'yOu', '?you-,!', 'y-o!u']
    expected = Counter({'you': 1, 'who': 1})
    assert count_keywords(text, keywords) == expected, \
    "Output should respect the keyword order and be unaffected"\
    "by capitalization and punctuation in the keywords!"

def test_count_keywords_no_occurence_keyword():
    text = "who are you with?"
    keywords = ['apple', 'you']
    expected = Counter({'apple': 0, 'you': 1})
    assert count_keywords(text, keywords) == expected, \
    "Words with no occurence should have a count of 0!"

def test_count_keywords_white_space():
    text = "who are you with?"
    keywords = ['', ' ', '  ']
    expected = Counter({'': 0})
    assert count_keywords(text, keywords) == expected, \
    "White-space only should be treated as empty string"

def test_count_keywords_punctuations_only():
    text = "who are you with?"
    keywords = ['?-,!']
    expected = Counter({'': 0})
    assert count_keywords(text, keywords) == expected, \
    "Punctuations-only should be treated as empty string (not a meaningful word)."

def test_count_keywords_empty_sentence():
    text = ""
    keywords = ['a', 'b', '', '   ']
    expected = Counter({'a': 0, 'b': 0, '': 0})

    text2 = " "
    assert count_keywords(text, keywords) == expected and \
    count_keywords(text2, keywords) == expected, \
    "White-space only sentence should return 0 count for everything (including empty strings)."