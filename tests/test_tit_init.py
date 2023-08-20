import os
from typer.testing import CliRunner
from tit.commands.tit_init import app

runner = CliRunner()


def test_tit_init_no_git():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_git():
    # Create a temporary .git directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".git")
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "this seems to be a git repository." in result.output
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_git_no_create():
    # Create a temporary .git directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".git")
        result = runner.invoke(app, input="n\n")
        assert result.exit_code == 0
        assert "this seems to be a git repository." in result.output
        assert "didn't Initialize a tit repo" in result.output


def test_tit_init_existing_git_create():
    # Create a temporary .git directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".git")
        result = runner.invoke(app, input="y\n")
        assert result.exit_code == 0
        assert "this seems to be a git repository." in result.output
        assert "Initialized an empty tit repository" in result.output


def test_tit_init_existing_tit():
    # Create a temporary .tit directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".tit")
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "a tit repo already exist." in result.output


def test_tit_init_existing_tit_no_create():
    # Create a temporary .tit directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".tit")
        result = runner.invoke(app, input="n\n")
        assert result.exit_code == 0
        assert "a tit repo already exist." in result.output


def test_tit_init_existing_tit_create():
    # Create a temporary .tit directory for testing
    with runner.isolated_filesystem():
        os.mkdir(".tit")
        result = runner.invoke(app, input="y\n")
        assert result.exit_code == 0
        assert "a tit repo already exist." in result.output
