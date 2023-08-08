import typer

app = typer.Typer()


def version_callback(value: bool):
    """
    Report current version of ZAQ - Version Control System package.
    """
    __version__ = "0.1.0"
    if value:
        typer.echo(f"ZAQ Version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Report current version of zaq package.",
    )
):
    return


@app.command()
def zaq():
    print(f"Zaq is the temporary name of this project.")


if __name__ == "__main__":
    app()
