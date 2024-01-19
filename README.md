# Wordwright

A package for text processing

## About

This Python package `wordwright` focuses on text analysis and processing. It offers a range of functions, from basic text cleaning to more complex analyses such as language detection, word and sentence counting, word frequency summarizing, and keyword searching. This functionality is particularly useful in fields like data analysis, natural language processing, and anywhere textual data needs to be understood or transformed. Functions are designed to be self-explanatory, which is especially beneficial for those new to programming or text processing.

## Installation

### Prerequisites

### Step 1: Create and Activate the Conda Environment

Create a new Conda environment using the environment.yaml file provided in this repository. This file contains all the necessary dependencies, including Python and Poetry versions.

To create the environment, open your terminal and navigate to the directory where the environment.yaml file is located. Then, run the following command:

``` bash
$ conda env create -f environment.yaml
```

This command will create a new Conda environment named 524 and install the specified dependencies.

Once the environment is created, you need to activate it using the following command:

``` bash
$ conda activate 524
```

### Step 2: Install the Package Using Poetry

With the Conda environment activated, you can now use Poetry to install the package. Ensure that the environment is activated (you should see (524) in your terminal prompt).

Run the following command to install the package using Poetry:

``` bash
$ poetry install
```

This command reads the pyproject.toml file in your project (if present) and installs the dependencies listed there.

### Troubleshooting

**Environment Creation Issues**: If you encounter problems while creating the Conda environment, ensure that the environment.yaml file is in the correct directory and that you have the correct version of Conda installed.

**Poetry Installation Issues**: If poetry install fails, verify that Poetry is correctly installed in the Conda environment and that your pyproject.toml file is properly configured.

## Usage

### Using this package

To use the `wordwright` package, you can import can call its functions in your Python scripts. 
Here is an example:

``` bash
from wordwright.preprocessing import clean_text
from wordwright.wordwright import count_keywords

text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
stopwords = ["the", "over", "was", "very"]
frequent_words(text, stopwords)
# Counter({'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 'lazy': 1, 'dog': 1})

from wordwright.wordwright import count_keywords
count_keywords("I like cheese.", ["cheese"])
# {'cheese': 1}
```

## Functions

-   `load_text(file_path)`: Loads and returns the content of a text file. Required input is `file_path`, which specifies the path to the file.

-   `clean_text(text)`: Cleans a text string by removing punctuation, converting to lowercase, and removing common stopwords. Required input is `text`, which is the string to be cleaned.

-   `count_keywords(text, keywords)`: Counts the occurrences of specified keywords in the text. Required inputs are `text` and `keywords`. After giving a list of keywords, this function return the occurrence of each selected word.

-   `count_sentences(text, punctuation)`: Count the number of sentences in the text. The number of sentences is counted based on specified delimiters. Required inputs are `text` and `punctuation`.

-   `language_detection(text)`: Detects if the text is in English or not. Required input is `text`, which is the text to be checked for language.

-   `frequent_words(text, number, stopwards)`: Analyzes a given text to find and return the most frequent words, excluding specified stopwords. Required inputs are `text`, `number`, and `stopwards`, which are the cleaned text to be analyzed, the number of most frequent words to return, and a list of words to be excluded from the analysis.

## `wordwright` Use in Python Ecosystem

While there are other packages that offer similar functions, such as [Natural Language Toolkit](https://www.nltk.org/) and [TextBlob](https://textblob.readthedocs.io/en/dev/). `wordwright` distinguishes itself by its simplicity and focus on the most essential text processing features. It is designed for ease of use, making it an excellent choice for those who have basic programming knowledge.

## Contributors

Yi Han (@yhan178)

Yingzi Jin (@jinyz8888)

Yi Yan (@carrieyanyi)

Hongyang Zhang (@alexzhang0825)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`wordwright` was created by Yi Han, Yingzi Jin, Yi Yan, Hongyang Zhang. It is licensed under the terms of the MIT license.

## Credits

`wordwright` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
