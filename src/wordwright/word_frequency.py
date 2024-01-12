def frequent_words(text, number, stopwords):
    """Analyzes a given text to find and return the most frequent words, 
    excluding specified stopwords.
    
    Parameters
    ----------
    text : str
        The cleaned text to be analyzed.
    number: int
        The number of most frequent words to return.
    stopwords: list of str
        A list of words to be excluded from the analysis.
    
    Returns
    -------
    collections.Counter
        A Counter object containing the most frequent words in the text 
        and their counts, excluding the specified stopwords.

    Example:
    >>> from collections import Counter
    >>> text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    >>> stopwords = ["the", "over", "was", "very"]
    >>> frequent_words(text, 3, stopwords)
    Counter({'quick': 2, 'fox': 2, 'brown': 1})
    """
    pass
