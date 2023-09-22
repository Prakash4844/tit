from typer.testing import CliRunner
from main import app
import tempfile
import os

runner = CliRunner()


def test_tit_use_valid_vcs():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")

        # Capture the printed output
        result = runner.invoke(app, ["use", "git"])
        # Assert exit code
        assert result.exit_code == 0


def test_tit_use_invalid_vcs():
    result = runner.invoke(app, ["use", "svn"])
    assert result.exit_code == 0
    assert "INVALID: svn VCS not supported." in result.output


def test_tit_use_already_set_up():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir(".git")
        with open(".git/tit_config.yaml", "w+") as file:
            file.write("Repo_type: \".git\"")
        result = runner.invoke(app, ["use", "git"])
        assert result.exit_code == 0
        assert "Already set up to use git repo" in result.output
