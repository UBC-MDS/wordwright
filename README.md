# textprocessing_group4

This package is built on top of an existing one `pycounts` (https://pypi.org/project/pycounts/) with additional features that were not included and we think are useful. On top of counting the number of the words, we have added features that allow the user to eliminate common stop words, count occurences of a given set of words, detect if the text is of English language or not, and count the number of sentences and total length of the text.

Our package is similar to `pycounts` and allows the user to conduct word counts for texts, but it is further elaborated so that it can produce results that are more interesting and meaningful in the context of English language by eliminating common stop words such as "a", "the", "and". Additionally, the features to count a given set of words and number of sentences allow the user to get more information of the text file.

## Functions
- load_text(file_path):

Loads and returns the content of a text file.
file_path: A string specifying the path to the file.

- clean_text(text):

Cleans a text string by removing punctuation, converting to lowercase, and removing common stopwords. Also generates a word cloud of the top 10 frequent words.
text: The text string to be cleaned.

- count_keywords(text, keywords):

Count the occurrences of each keyword in the given text.
`text`: The text in which to count keywords. 
`keywords`: A list of keywords to search for.

- count_sentences_and_length(text):

Counts the number of sentences and calculates the total length of the given text.
text: The text to be analyzed.

- language_detection(text):

Detects if the text is in English or not.
text: The text to be checked for language.

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
