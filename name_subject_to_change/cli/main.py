import typer

__version__ = "0.1.0"

app = typer.Typer(no_args_is_help=True, help=f"ZAQ - Version: {__version__}")


def vers(value: bool):
    """
    Report current version of ZAQ - Version Control System package.
    :param value: bool
    """
    if value:
        typer.echo(f"ZAQ Version: {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def app_callback():
    """
    Report current version of ZAQ - Version Control System package.
    :return:
    """
    typer.echo(f"ZAQ Version: {__version__}")
    raise typer.Exit()


@app.command()
def zaq():
    print(f"Zaq is the temporary name of this project.")


@app.callback()
def main(
        version: bool = typer.Option(
            None,
            "-v",
            "--version",
            callback=app_callback,
            is_eager=True,
            help="Report current version of zaq package.",
        )
):
    return


if __name__ == "__main__":
    app()
