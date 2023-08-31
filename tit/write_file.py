# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 31 Aug, 2023

def write_binary_file(path, data):
    """
    Write data bytes to file at given path.
    """
    with open(path, 'wb') as f:
        f.write(data)


def read_tit_config_yaml_file(path):
    try:
        with open(path) as f:
            repo_name = f.readline()
            if repo_name == 'Repo_type: ".git"':
                return True
    except FileNotFoundError:
        return False


def write_file(path, data):
    """
        Write text to file at given path.
    """
    with open(path, 'w+') as f:
        f.write(data)
