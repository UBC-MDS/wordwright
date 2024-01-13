# wordwright

This Python package `wordwright` focuses on text analysis and processing. It offers a range of functionalities, from basic text cleaning to more complex analyses including language detection, word and sentence counting, word frequency summarizing, and keyword searching. This functionality is particularly useful in fields like data analysis, natural language processing, and anywhere textual data needs to be understood or transformed. The functions are designed to be self-explanatory, which is especially beneficial for those new to programming or text processing. While packages like `pycounts` also provide similar functionalities, our more advanced features can provide users more meaningful and interesting results in the context of English language.

**wordwright Use in Python Ecosystem**
While there are other packages that offer similar functionalities, such as NLTK (Natural Language Toolkit [link](http://nltk.org/))) and TextBlob ([link](https://textblob.readthedocs.io/en/dev/)). `wordwright` distinguishes itself by its simplicity and focus on the most essential text processing features. `wordwright` is designed for ease of use, making it an excellent choice for those who require straightforward text processing capabilities without the overhead of more complex NLP frameworks.


## Functions

- `load_text(file_path)`: Load and return the content of a text file. Removing punctuation, converting to lowercase.

  - `file_path`: The path to the text file to be read.

- `clean_text(text)`: Clean a text string by removing punctuation and converting to lowercase.

  - `text`: The text to be cleaned.

- `count_keywords(text, keywords)`: Count the occurrences of each keyword in the given text.

  - `text`: The text in which to count keywords. 
  - `keywords`: A list of keywords to search for.

- `count_sentences_and_length(text, punctuation)`: Count the number of sentences and the total number of words in the text. The number of sentences based on specified delimiters.

  - `text`: The text to be analyzed.
  - `punctuation`: List of punctuation marks.

- `language_detection(text)`: Detect if the text is in English or not.

  - `text`: The text to be checked.

- `frequent_words(text, number, stopwords)`: Analyzes a given text to find and return the most frequent words, excluding specified stopwords.

  - `text`: The cleaned text to be analyzed.
  - `number`: The number of most frequent words to return.
  - `stopwords`: A list of words to be excluded from the analysis.

## Installation

```bash
$ pip install wordwright
```

## Usage

```
from textprocessing_group4.textprocessing_group4 import count_keywords
test = count_keywords("I like cheese.", ["cheese"])
```

## Contributors
Yi Han, Yingzi Jin, Yi Yan, Hongyang Zhang

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`textprocessing_group4` was created by Group 4. It is licensed under the terms of the MIT license.

## Credits

`textprocessing_group4` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
