import os
import tempfile
import datetime
import yaml
from tit.check_repo import current_datetime, check_if_repo, check_tit_config
from tit.write_file import write_file


def test_current_datetime():
    # Test if current_datetime() returns the expected formatted datetime
    expected_format = '%Y-%m-%d %H:%M:%S'
    current_time = datetime.datetime.now()
    formatted_current = current_time.strftime(expected_format)
    assert current_datetime() == formatted_current


def test_check_if_repo_no_repo():
    # Test when no repo exists
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        assert not check_if_repo()


def test_check_if_repo_tit_repo():
    # Test when a .tit repo exists
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".tit")
        assert check_if_repo()


def test_check_if_repo_git_repo_with_invalid_tit_config():
    # Test when a .git repo exists with an invalid tit_config.yaml
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        with open(os.path.join('.git', 'tit_config.yaml'), 'w') as file:
            file.write("invalid_yaml: basinful")
        assert not check_if_repo()


def test_check_if_repo_git_repo_with_valid_tit_config():
    # Test when a .git repo exists with a valid tit_config.yaml
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        write_file(".git/tit_config.yaml", 'Repo_type: ".git"')
        assert check_if_repo()


def test_check_if_repo_git_repo_with_valid_tit_config_wrong_type():
    # Test when a .git repo exists with a valid but wrong tit_config.yaml
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        with open(os.path.join('.git', 'tit_config.yaml'), 'w') as file:
            yaml_data = {'  Repo_type'  'asdf'  'invalid'}
            yaml.dump(yaml_data, file)
        assert not check_tit_config()


def test_check_if_repo_git_repo_with_no_tit_config():
    # Test when a .git repo exists with a valid but wrong tit_config.yaml
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        assert not check_tit_config()


def test_check_if_repo_mixed_case():
    # Test when both .git and .tit repos exist
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        os.mkdir(".tit")
        assert check_if_repo()


def test_check_if_repo_verbose(capsys):
    # Test verbose mode for check_if_repo()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".tit")
        check_if_repo(verbose=True)
        captured = capsys.readouterr()
        assert "tit repo found in" in captured.out  # Check if print was called

# Add more test cases as needed
