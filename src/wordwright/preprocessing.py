from string import punctuation
import os

def load_text(file_path):
    """ Load and return the content of a text file. 

    This function reads a text file from the specified file path, but 
    does not modify the content of the file.

    Parameters
    ----------    
    file_path: str 
        The path to the text file to be read.
    
    Returns
    ---------- 
    str
        The content of the file as a string.
    
    Raises
    ------
    FileNotFoundError
        If the file specified by file_path does not exist.
    OSError
        If there is an error opening or reading the file.

    Examples
    --------
    >>> load_text("text.txt")
    """
    try:
        with open(file_path, "r") as file:
            txt = file.read()
        return txt
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)

def clean_text(text):
    """
    Clean a text string by removing punctuation (except apostrophes), converting to 
    lowercase, and removing excessive spaces and tabs.

    Parameters
    ----------
    text : str
        The text to be cleaned.

    Returns
    ---------- 
    str
        The cleaned text.
    
    Examples
    --------
    >>> clean_text("It's a sunny day. ,Let's GO!")
    "it's a sunny day let's go"
    """
    if not isinstance(text, str):
        raise TypeError("The input must be a string.")

    modified_punctuation = punctuation.replace("'", "")

    txt = text.lower()
    for p in modified_punctuation:
        txt = txt.replace(p, "")

    # Split the text into words and join back together to remove excessive whitespace
    txt = ' '.join(txt.split())

    return txt