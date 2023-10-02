import os
import tempfile
from tit.write_file import write_binary_file, write_file


def test_write_binary_file():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        data = b"Hello, world!"
        write_binary_file(tmp_file_path, data)

    with open(tmp_file_path, "rb") as tmp_file_read:
        assert tmp_file_read.read() == data

    os.remove(tmp_file_path)


def test_write_file():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        data = "Hello, world!"
        write_file(tmp_file_path, data)

    with open(tmp_file_path, "r") as tmp_file_read:
        assert tmp_file_read.read() == data

    os.remove(tmp_file_path)

# Run the tests using the pytest command
