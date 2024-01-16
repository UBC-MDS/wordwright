def count_sentences(text, punctuation):
    """
    Count the number of sentences in the text, which is based on specified delimiters.
   
    Parameters
    ----------
    text (str)
        The text to be analyzed.
    punctuation (list)
        List of punctuation marks
    
    Returns
    ----------
    int
        An int describing the number of sentences in text.
    
    Examples
    --------
    >>> from wordwright.wordwright import count_sentences
    >>> test = count_sentences_and_length("I like cheese! I like cat. I hate fruit", ["!", "."])
    2
    
    """
    sentense_count = 0
    
    if type(punctuation) != list:
        raise TypeError("Please enter a list of punctuation")
        
    if text:
        for i in range(len(text)):
            for punc in punctuation:
                if text[i] == punc:
                    if text[i + 1] == ' ':
                        sentense_count += 1
    print(f"There are {sentense_count} sentense(s), which is splited by {punctuation}.")
    return sentense_count        