# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 31 Aug, 2023

def write_binary_file(path, data):
    """
    Write data bytes to file at given path.
    """
    with open(path, 'wb') as f:
        f.write(data)


def write_file(path, data):
    """
        Write text to file at given path.
    """
    with open(path, 'w+') as f:
        f.write(data)
