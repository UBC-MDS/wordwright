from wordwright import count_sentences_and_length 


def test_empty_string():
    text = ""
    punctuation = ["."]
    assert count_sentences_and_length(text, punctuation) == (0, 0)

def test_no_punctuation_input():
    text = "xcxccfssgjkvvhjmbh"
    punctuation = ["."]
    assert count_sentences_and_length(text, punctuation) == (0, 1)

def test_invalid_punctuation_input():
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = "."
    assert count_sentences_and_length(text, punctuation) == False, "Invalid punctuation input. Should be a list of punctuation"

def test_multiple_sentence():
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = [".", "?", "!"]
    assert count_sentences_and_length(text, punctuation) == (3, 9)

def test_multiple_occurrences(self):
    text = "Exciting!!! Really exciting!!! Isn't it?"
    punctuation = ["?", "!"]
    assert count_sentences_and_length(text, punctuation) == (3, 5)