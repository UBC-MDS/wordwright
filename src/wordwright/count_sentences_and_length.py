def count_sentences_and_length(text, punctuation):
    """
    Count the number of sentences and the total number of words in the text. 
    The number of sentences based on specified delimiters.
   
    Parameters
    ----------
    text (str)
        The text to be analyzed.
    punctuation (list)
        List of punctuation marks.
    
    Returns
    ----------
    tuple
        A tuple containing the number of sentences and the total word length in text.
    
    Examples
    --------
    >>> from wordwright.wordwright import count_sentences_and_length
    >>> test = count_sentences_and_length("I like cheese! I like cat. I hate fruit", ["!", "."])
    (2, 6)
    
    """
    # Function code...