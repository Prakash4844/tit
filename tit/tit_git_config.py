def read_tit_config_yaml_file(path):
    try:
        with open(path) as f:
            repo_name = f.readline()
            if repo_name == 'Repo_type: ".git"':
                return True
            elif repo_name != 'Repo_type: ".git"':
                print("tit config file found, but doesn't contain any supported VCS")
                return False
    except FileNotFoundError:
        return False
