from typer.testing import CliRunner
from main import app

runner = CliRunner()


def test_version_option():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "TIT Version" in result.stdout


def test_help_option():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "TIT: Version Control System" in result.stdout
