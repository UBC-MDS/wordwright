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
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
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
    counts = {keyword: sum(1 for _ in re.finditer(r'\b{}\b'.format(re.escape(keyword)), text, re.IGNORECASE))
              for keyword in keywords}
    return counts


def count_sentences_and_length(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    text_length = len(text)
    return num_sentences, text_length


def language_detection(text):
    try:
        return "English" if detect(text) == 'en' else "Not English"
    except:
        return "Language detection error"

