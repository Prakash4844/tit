from tit.tit_git_config import read_tit_config_yaml_file
import tempfile
import os


def test_read_tit_config_yaml_file():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        repo_type = 'Repo_type: ".git"'
        tmp_file.write(repo_type.encode())
        tmp_file.close()

        assert read_tit_config_yaml_file(tmp_file_path)
        os.remove(tmp_file_path)

    # Test case when file doesn't exist
    assert not read_tit_config_yaml_file("nonexistent.yaml")


def test_read_tit_invalid_config(capsys):
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        with open(os.path.join('.git', 'tit_config.yaml'), 'w'):
            read_tit_config_yaml_file("./.git/tit_config.yaml")
            captured = capsys.readouterr()
            assert "tit config file found, but doesn't contain any supported VCS" in captured.out
