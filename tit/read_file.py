# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 2 Oct, 2023
# Comments: Happy Birthday Lal Bahadur Shastri and Mahatma Gandhi

def read_binary_file(path):
    """Read contents of file at given path as bytes."""
    with open(path, 'rb') as f:
        return f.read()
