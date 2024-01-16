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
        load_text("nonexistent_file.txt")
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError not raised for nonexistent file"

def test_load_invalid_file_path():
    # Test loading with an invalid file path
    try:
        load_text("")
    except OSError:
        pass
    else:
        assert False, "OSError not raised for invalid file path"

# Clean up the test file after tests
os.remove(test_file_name)