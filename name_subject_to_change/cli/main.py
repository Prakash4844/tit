import typer

__version__ = "0.0.1"

app = typer.Typer(
    name="zaq",
    no_args_is_help=True,
    add_completion=False,
    invoke_without_command=True,
    help=f"ZAQ: Version Control System. \n\nVersion: {__version__}",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.callback(invoke_without_command=True)
def get_version(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Print version and exit.",
    ),
) -> None:
    """Display the version."""
    if version:
        typer.echo(f"ZAQ Version: {__version__}")
        raise typer.Exit()


if __name__ == "__main__":
    app()
