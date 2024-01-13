import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from langdetect import detect
from nltk.tokenize import sent_tokenize
nltk.download('punkt')


def language_detection(text):
    """Detect if the text is in English or not.

    Parameters
    ----------
    text : str
        The text to be checked.

    Returns
    -------
    str: "English" if the text is detected to be in English, "Not English" otherwise,
         or "Language detection error" in case of an error.

    Examples
    --------
    >>> language_detection("test text2")
    English
    """
    pass
