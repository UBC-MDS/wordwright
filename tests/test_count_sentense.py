from wordwright import count_sentences 


def test_empty_string():
    """
    Test that an empty string returns a sentence count of 0.
    """
    text = ""
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentenses counted incorrectly"

def test_no_punctuation_input():
    """
    Test that a string with no punctuation marks returns a sentence count of 0.
    """
    text = "xcxccfssgjkvvhjmbh"
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentenses counted incorrectly"

def test_invalid_punctuation_input():
    """
    Test that passing a non-list punctuation argument returns False.
    """
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = "!"
    assert count_sentences(text, punctuation) == False, "Invalid punctuation input. Should be a list of punctuation"

def test_multiple_sentence_endings():
    """
    Test that the function counts sentences correctly with multiple sentence endings.
    """
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = [".", "?", "!"]
    assert count_sentences(text, punctuation) == 3, "Sentenses counted incorrectly"

def test_multiple_occurrences(self):
    """
     Test that the function counts multiple occurrences of punctuation marks as separate sentences.
    """
    text = "Exciting!!! Really exciting!!! Isn't it?"
    punctuation = ["?", "!"]
    assert count_sentences(text, punctuation) == 3, "Sentenses counted incorrectly"