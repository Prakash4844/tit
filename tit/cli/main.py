import typer
from tit import __version__  # Importing the version information from the 'tit' module

# Create a Typer app instance.
# Set the app's help message with the version information.
app = typer.Typer(
    name="tit",
    no_args_is_help=True,
    add_completion=False,
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


# Execute the Typer app when the script is run directly
if __name__ == "__main__":
    app()  # Run the Typer app
