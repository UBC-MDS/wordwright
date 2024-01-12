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

def load_text(file_path):
    """
    Load and return the content of a text file.

    Parameters:
    file_path (str): The path to the text file to be read.

    Returns:
    str: The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
    """
    Clean a text string by removing punctuation, converting to lowercase, 
    and removing common stopwords. Then generate and display a word cloud of the top 10 frequent words.

    Parameters:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove common words (stopwords)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    cleaned_text = ' '.join([word for word in words if word not in stop_words])

    # Word frequency
    word_freq = Counter(cleaned_text.split())

    # Word cloud of top 10 frequent words
    wc = WordCloud(width=800, height=400, max_words=10).generate_from_frequencies(word_freq)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    return cleaned_text

def count_keywords(text, keywords):
    """
    Count the occurrences of each keyword in the given text.

    Parameters:
    text (str): The text in which to count keywords.
    keywords (list of str): A list of keywords to count in the text.

    Returns:
    dict: A dictionary where keys are keywords and values are the counts of those keywords in the text.
    """
    counts = {keyword: sum(1 for _ in re.finditer(r'\b{}\b'.format(re.escape(keyword)), text, re.IGNORECASE))
              for keyword in keywords}
    return counts


def count_sentences_and_length(text):
    """
    Count the number of sentences and calculate the total length of the text.

    Parameters:
    text (str): The text to be analyzed.

    Returns:
    tuple: A tuple containing the number of sentences and the total text length.
    """
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    text_length = len(text)
    return num_sentences, text_length


def language_detection(text):
    """
    Detect if the text is in English or not.

    Parameters:
    text (str): The text to be checked.

    Returns:
    str: "English" if the text is detected to be in English, "Not English" otherwise, 
         or "Language detection error" in case of an error.
    """
    try:
        return "English" if detect(text) == 'en' else "Not English"
    except:
        return "Language detection error"

