import pytest
from wordwright.preprocessing import load_text

# Set up a temporary text file for testing
test_file_name = "test_file.txt"
with open(test_file_name, 'w') as file:
    file.write("Hello, World!")

def test_load_existing_file():
    """
    Test loading an existing file
    
    This test verifies that the load_text function correctly reads and 
    returns the content of an existing file.
    """
    content = load_text(test_file_name)
    assert content == "Hello, World!", "Should correctly read file contents"

def test_load_nonexistent_file():
    """
    Test loading a file that does not exist
    
    This test ensures that the load_text function raises a FileNotFoundError 
    when trying to load a file that does not exist. 
    """
    with pytest.raises(FileNotFoundError):
        file_path = "nonexistent_file.txt"
        load_text(file_path)

def test_load_invalid_file_path():
    """
    Test loading with an invalid file path
    
    This test checks that the load_text function raises a TypeError when the 
    input is not a valid file path, such as a non-string value. 
    """
    with pytest.raises(TypeError):
        load_text(123)
