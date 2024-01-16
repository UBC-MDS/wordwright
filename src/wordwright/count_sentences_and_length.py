from wordwright import clean_text

def count_sentences_and_length(text, punctuation):
    """
    Count the number of sentences and the total number of words in the text. 
    The number of sentences based on specified delimiters.
   
    Parameters
    ----------
    text (str)
        The text to be analyzed.
    punctuation (list)
        List of punctuation marks
    
    Returns
    ----------
    tuple
        A tuple containing the number of sentences and the total word length in text.
    
    Examples
    --------
    >>> from wordwright.wordwright import count_sentences_and_length
    >>> test = count_sentences_and_length("I like cheese! I like cat. I hate fruit", ["!", "."])
    (2, 9)
    
    """
    sentense_count = 0
    word_count = 0
    
    if type(punctuation) != list:
        raise TypeError("Please enter a list of punctuation")
        
    if text:
        for i in range(len(text)):
            for punc in punctuation:
                if text[i] == punc:
                    if text[i + 1] == ' ':
                        sentense_count += 1
    #word_count = len(clean_text(text).split(" "))
    
    print(f"There are {sentense_count} sentenses, which is splited by {punctuation}.")
    print(f"There are a total of {word_count} words in the text.") 
    
    return (sentense_count, word_count)         