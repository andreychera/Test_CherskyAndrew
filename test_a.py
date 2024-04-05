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

@pytest.mark.parametrize("keyword, expected_output", [
    ("test", "This is a test file.\n"),
    ("keyword", "Keyword is important here.\n"),
    ("not_found", ""),
])
def test_filter_file(temp_file, keyword, expected_output, tmpdir):
    output_file_path = tmpdir.join("test_output.txt")
    filter_file(temp_file, output_file_path, keyword)
    with open(output_file_path, "r") as f:
        output_content = f.read()
    assert output_content.strip().lower() == expected_output.strip().lower()