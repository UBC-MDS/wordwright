import os
from wordwright.preprocessing import load_text

# Set up a temporary text file for testing
test_file_name = "test_file.txt"
with open(test_file_name, 'w') as file:
    file.write("Hello, World!")

def test_load_existing_file():
    # Test loading an existing file
    content = load_text(test_file_name)
    assert content == "Hello, World!", "Should correctly read file contents"

def test_load_nonexistent_file():
    # Test loading a file that does not exist
    try:
        file_path = "nonexistent_file.txt"
        load_text(file_path)
    except FileNotFoundError as e:
        assert str(e) == f"[Errno 2] No such file or directory: {file_path}", "FileNotFoundError expected"

def test_load_invalid_file_path():
    # Test loading with an invalid file path
    try:
        load_text(123)
    except OSError as e:
        assert str(e) == "[Errno 9] Bad file descriptor", "OSError with message '[Errno 9] Bad file descriptor' expected"
