import os 
import pytest

from main import filter_file

@pytest.fixture
def temp_file(tmpdir):
    input_content = """this is a test file.
    it contains some lines.
    these lines may or may not contain the keyword.
    keyword is important here.
    but not here."""
    input_file_path = tmpdir.join("test_input.txt")
    with open(input_file_path, "w") as f:
        f.write(input_content)
    return input_file_path