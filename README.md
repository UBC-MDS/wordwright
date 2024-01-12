# wordwright

This package is built on top of an existing one `pycounts` (https://pypi.org/project/pycounts/) with additional features that were not included and we think are useful. On top of counting the number of the words, we have added features that allow the user to eliminate common stop words, count occurences of a given set of words, detect if the text is of English language or not, and count the number of sentences and total length of the text.

Our package is similar to `pycounts` and allows the user to conduct word counts for texts, but it is further elaborated so that it can produce results that are more interesting and meaningful in the context of English language by eliminating common stop words such as "a", "the", "and". Additionally, the features to count a given set of words and number of sentences allow the user to get more information of the text file.

## Functions

- load_text(file_path):

Load and return the content of a text file. Removing punctuation, converting to lowercase.

- `file_path`: The path to the text file to be read.

- clean_text(text):

Clean a text string by removing punctuation and converting to lowercase.

- `file_path`: The text to be cleaned.

- count_keywords(text, keywords):

Count the occurrences of each keyword in the given text.

- `text`: The text in which to count keywords. 
- `keywords`: A list of keywords to search for.

- count_sentences_and_length(text):

Count the number of sentences and the total number of words in the text. The number of sentences based on specified delimiters.

- `text`: The text to be analyzed.
- `punctuation`: List of punctuation marks.

- language_detection(text):

Detect if the text is in English or not.

- `text`: The text to be checked.

- frequent_words(text, number, stopwords):

Analyzes a given text to find and return the most frequent words, excluding specified stopwords.

- `text`: The cleaned text to be analyzed.
- `number`: The number of most frequent words to return.
- `stopwords`: A list of words to be excluded from the analysis.

## Installation

```bash
$ pip install textprocessing_group4
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
