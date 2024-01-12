# textprocessing_group4

A package for text processing

## Functions
- load_text(file_path):

Loads and returns the content of a text file.
file_path: A string specifying the path to the file.

- clean_text(text):

Cleans a text string by removing punctuation, converting to lowercase, and removing common stopwords. Also generates a word cloud of the top 10 frequent words.
text: The text string to be cleaned.

- count_keywords(text, keywords):

Counts the occurrences of specified keywords in the text.
text: The text in which to count keywords. keywords: A list of keywords to search for.

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

- TODO

## Contributors
Yi Han, Yi Yan, Hongyang Zhang, Yingzi Jin

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`textprocessing_group4` was created by Group 4. It is licensed under the terms of the MIT license.

## Credits

`textprocessing_group4` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
