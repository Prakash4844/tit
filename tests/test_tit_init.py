from typer.testing import CliRunner
from main import app
import tempfile
import os


runner = CliRunner()


def test_tit_init():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        # Test tit init without force or verbose
        result = runner.invoke(app, ["init"])
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_force():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.git')
        # Test tit init with force option
        result = runner.invoke(app, ["init", "--force"])
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_verbose():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        # Test tit init with verbose option
        result = runner.invoke(app, ["init", "--verbose"])
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_repo():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".tit")
        # Test tit init when a .tit repo already exists
        result = runner.invoke(app, ["init"])
        assert result.exit_code == 0


def test_tit_init_existing_repo_force():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.tit')
        # Test tit init when a .tit repo already exists with force option
        result = runner.invoke(app, ["init", "--force"])
        assert "a tit repo already exist." in result.output


def test_tit_init_existing_git_repo():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.git')
        # Test tit init when a .git repo already exists
        result = runner.invoke(app, ["init"])
        assert "This seems to be a git repository" in result.output


def test_tit_init_existing_git_repo_force():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.git')
        # Test tit init when a .git repo already exists with force option
        result = runner.invoke(app, ["init", "--force"])
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_git_repo_verbose():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.git')
        # Test tit init when a .git repo already exists with verbose option
        result = runner.invoke(app, ["init", "--verbose"])
        assert "This seems to be a git repository" in result.output


def test_tit_init_verbose_force():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('.git')
        # Test tit init when a .git repo already exists with verbose option
        result = runner.invoke(app, ["init", "--verbose", "--force"])
        assert "Initialized an empty tit repository" in result.output

