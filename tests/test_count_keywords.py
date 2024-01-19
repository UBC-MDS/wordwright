import pytest
from collections import Counter
from wordwright.count_keywords import count_keywords

def test_count_keywords_non_string_text():
    """
    Test whether count_keywords throws a type error if user inputs a 
    non-string for the text.
    """
    with pytest.raises(TypeError):
        count_keywords(123, ['123'])
    with pytest.raises(TypeError):
        count_keywords([123], ['123'])
    with pytest.raises(TypeError):
        count_keywords(True, ['123'])

def test_count_keywords_non_list_keywords():
    """
    Test whether count_keywords throws a type error if user inputs a 
    non-list for the keywords.
    """
    with pytest.raises(TypeError):
        count_keywords('ab', '123')
    with pytest.raises(TypeError):
        count_keywords('ab', 123)
    with pytest.raises(TypeError):
        count_keywords('ab', True)
    with pytest.raises(TypeError):
        count_keywords('ab', {'cheese': 'sticks'})

def test_count_keywords_non_string_keyword():
    """
    Test whether count_keywords throws a type error if user inputs a 
    keyword list containing non-string variables.
    """
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
    """
    Test whether count_keywords produces the output correctly with a
    basic text.
    """
    text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    keywords = ['the', 'dog', 'quick']
    expected = Counter({'the': 3, 'dog': 1, 'quick': 2})
    assert count_keywords(text, keywords) == expected, "Incorrect output!"

def test_count_keywords_correct_keyword_order():
    """
    Test whether count_keywords' output preserves the keyword order
    that was given in the keyword list.
    """
    text = "alpha bravo charlie delta"
    keywords = ['delta', 'charlie', 'bravo', 'alpha']
    expected = Counter({'delta': 1, 'charlie': 1, 'bravo': 1, 'alpha': 1})
    assert count_keywords(text, keywords) == expected, "Incorrect keyword order!"

def test_count_keywords_unique_keyword_output():
    """
    Test whether count_keywords' output only shows the number of 
    occurence for a word once, even if the word appears multiple
    times in the user-provided list.
    """
    text = "who are you with?"
    keywords = ['you!', 'who', 'You', 'you', 
                'yOu', '?you-,!', 'y-o!u']
    expected = Counter({'you': 1, 'who': 1})
    assert count_keywords(text, keywords) == expected, \
    "Output should respect the keyword order and be unaffected"\
    "by capitalization and punctuation in the keywords!"

def test_count_keywords_no_occurence_keyword():
    """
    Test whether count_keywords returns 0 count for words that
    never occurs in the text.
    """
    text = "who are you with?"
    keywords = ['apple', 'you']
    expected = Counter({'apple': 0, 'you': 1})
    assert count_keywords(text, keywords) == expected, \
    "Words with no occurence should have a count of 0!"

def test_count_keywords_white_space():
    """
    Test whether count_keywords considers any number of white-spaces
    empty strings.
    """
    text = "who are you with?"
    keywords = ['', ' ', '  ']
    expected = Counter({'': 0})
    assert count_keywords(text, keywords) == expected, \
    "White-space only should be treated as empty string!"

def test_count_keywords_punctuations_only():
    """
    Test whether count_keywords considers any string with punctuations
    only empty strings.
    """
    text = "who are you with?"
    keywords = ['?-,!']
    expected = Counter({'': 0})
    assert count_keywords(text, keywords) == expected, \
    "Punctuations-only words should be treated as empty string (not a meaningful word)!"

def test_count_keywords_empty_sentence():
    """
    Test whether count_keywords returns 0 count for all words if the text
    given is empty or only contains white spaces.
    """
    text = ""
    keywords = ['a', 'b', '', '   ']
    expected = Counter({'a': 0, 'b': 0, '': 0})

    text2 = " "
    assert count_keywords(text, keywords) == expected and \
    count_keywords(text2, keywords) == expected, \
    "White-space only sentence should return 0 count for everything (including empty strings)!"

def test_count_keywords_punctuation_sentence():
    """
    Test whether count_keywords considers a text with only punctuations
    an empty string.
    """
    text = "---!!!--!"
    keywords = ['---!!!--!', 'a']
    expected = Counter({'': 0, 'a': 0})
    assert count_keywords(text, keywords) == expected, \
    "Punctuations only sentences should be considered empty strings!"

def test_count_keywords_trapped_word():
    """
    Test whether count_keywords a word trapped in punctuations a word
    in the text.
    """
    text = "y!-o!u"
    keywords = ['you']
    expected = Counter({'you': 1})
    assert count_keywords(text, keywords) == expected, \
    "Trapped word should be a considered a word!"