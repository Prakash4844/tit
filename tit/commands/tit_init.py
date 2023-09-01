# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit init
# date: 20 Aug, 2023

import os
import typer
from rich import print
from typer import Typer
from typing_extensions import Annotated
from tit.write_file import write_binary_file
from tit.check_repo import current_datetime, check_if_repo

# create a typer app using required data.
app = Typer(
    help="tit init: Create an empty Tit repository or reinitialize an existing one",
    context_settings={"help_option_names": ["-h", "--help"]}
)


def create_repo(verbose: bool = False) -> None:
    """
    creates an empty .tit repo
    :param verbose: enables verbose logging
    :return:
    """
    if verbose:
        print(f"[green]{current_datetime()}[/green]: making a empty tit repository in [blue]{os.getcwd()}[blue]")
    try:
        os.mkdir(os.path.join('.tit'))
        for name in ['objects', 'refs', 'refs/heads']:
            os.mkdir(os.path.join('.tit', name))
        write_binary_file(os.path.join('.tit', 'HEAD'),
                          b'ref: refs/heads/main')
        print(f"Initialized an empty tit repository in [blue]{os.getcwd()}[blue]")
    except FileExistsError:
        print("a tit repo already exist.")


@app.callback(invoke_without_command=True)
def tit_init(
        force: Annotated[bool, typer.Option(
            "--force",
            "-f",
            help="Use force option to ignore git repo existence."
        )] = False,
        verbose: Annotated[bool, typer.Option(
            "--verbose",
            "-v",
            help="Enable verbose mode."
        )] = False
):
    """
    tit init: Create an empty Tit repository or reinitialize an existing one.
    :param: force: use force option to ignore git repo existence.
    :param: verbose: enables verbose logging
    :return:
    """

    if force and not verbose:
        create_repo()
        exit(0)
    elif force and verbose:
        create_repo(verbose=verbose)
        exit()

    is_git_repo = check_if_repo(verbose=verbose)

    if not is_git_repo:
        if verbose:
            create_repo(verbose=verbose)
        else:
            create_repo()
    else:
        exit(0)


if __name__ == "__main__":
    app()
