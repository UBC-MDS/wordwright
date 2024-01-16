from wordwright.preprocessing import clean_text
from collections import Counter

def frequent_words(text, stopwords=[]):
    """Analyzes a given text to find the count of unique words, 
    excluding specified stopwords.
    
    Parameters
    ----------
    text : str
        The cleaned text to be analyzed.
    stopwords: list of str
        A list of words to be excluded from the analysis.
    
    Returns
    -------
    collections.Counter
        A Counter object containing the words in the text 
        and their counts, excluding the specified stopwords.

    Example:
    >>> from wordwright.preprocessing import clean_text
    >>> from collections import Counter
    >>> text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    >>> stopwords = ["the", "over", "was", "very"]
    Counter({'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 'lazy': 1, 'dog': 1})
    """
    if not isinstance(text, str):
        raise TypeError("The input must be a string.")

    if not isinstance(stopwords, list):
        raise TypeError("The input must be a list.")
    if not all(isinstance(word, str) for word in stopwords):
        raise TypeError("All items in the 'stopwords' list must be strings.")
    
    text = clean_text(text)
    words = text.split()
    word_counts = Counter(words)
    
    for stopword in stopwords:
        word_counts.pop(stopword, None)
    
    return word_counts
