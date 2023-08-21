from typer.testing import CliRunner
from main import app
import os

runner = CliRunner()


def test_tit_init_existing_git():
    # Create a temporary .git directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".git")  # Create a .git directory
        result = runner.invoke(app, ["init"])
        assert result.exit_code == 0
        assert "This seems to be a git repository." in result.output


def test_tit_init_existing_git_force():
    # Create a temporary .git directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".git")  # Create a .git directory
        result = runner.invoke(app, ["init", "--force"])
        assert result.exit_code == 0
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_not_git_repo():
    with runner.isolated_filesystem():
        result = runner.invoke(app, ["init"])
        assert result.exit_code == 0
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_force_not_git_repo():
    with runner.isolated_filesystem():
        result = runner.invoke(app, ["init", "--force"])
        assert result.exit_code == 0
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_tit_repo():
    # Create a temporary .tit directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".tit")  # Create a .tit directory
        result = runner.invoke(app, ["init"])
        assert result.exit_code == 0
        assert "a tit repo already exist." in result.output


def test_tit_init_verbose_existing_tit_repo():
    # Create a temporary .tit directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".tit")  # Create a .tit directory
        result = runner.invoke(app, ["init", "--verbose"])
        assert result.exit_code == 0
        assert "a tit repo already exist." in result.output

# Add more test cases as needed
