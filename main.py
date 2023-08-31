import typer
from tit import __version__
from tit.commands import tit_init, tit_use

# Create a Typer app instance.
# Set the app's help message with the version information.
app = typer.Typer(
    name="tit",
    no_args_is_help=True,
    invoke_without_command=True,
    help=f"TIT: Version Control System. \n\nVersion: {__version__}",
    context_settings={"help_option_names": ["-h", "--help"]},
)


# Define a callback function to display the version information
@app.callback(invoke_without_command=True)
def get_version(
        version: bool = typer.Option(
            False,
            "--version",
            "-v",
            help="Print version and exit.",  # Help message for the version option
        ),
) -> None:
    """
    Display the version of tit - Version Control System.
    """
    if version:
        typer.echo(f"TIT Version: {__version__}")  # Print the version information if the version option is provided
        raise typer.Exit()  # Exit the application


# -----------------Commands----------------------

app.add_typer(tit_init.app, name="init")
app.add_typer(tit_use.app, name="use")

# Execute the Typer app when the script is run directly
if __name__ == "__main__":
    app()  # Run the Typer app
