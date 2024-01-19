from wordwright import count_sentences 


def test_empty_string():
    text = ""
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentenses counted incorrectly"

def test_no_punctuation_input():
    text = "xcxccfssgjkvvhjmbh"
    punctuation = ["."]
    assert count_sentences(text, punctuation) == 0, "Sentenses counted incorrectly"

def test_invalid_punctuation_input():
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = "!"
    assert count_sentences(text, punctuation) == False, "Invalid punctuation input. Should be a list of punctuation"

def test_multiple_sentence_endings():
    text = "Hello world! It's a beautiful day? Yes, it is."
    punctuation = [".", "?", "!"]
    assert count_sentences(text, punctuation) == 3, "Sentenses counted incorrectly"

def test_multiple_occurrences(self):
    text = "Exciting!!! Really exciting!!! Isn't it?"
    punctuation = ["?", "!"]
    assert count_sentences(text, punctuation) == 3, "Sentenses counted incorrectly"