# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit init
# date: 20 Aug, 2023

import os
import datetime
import typer
from typer import Typer
from typing_extensions import Annotated


def current_datetime():
    """
    :return: current datetime
    """
    return datetime.datetime.now()


# create a typer app using required data.
app = Typer(
    help="tit init: Create an empty Tit repository or reinitialize an existing one",
    context_settings={"help_option_names": ["-h", "--help"]}
)


def check_if_git_repo(verbose: bool = False) -> bool:
    """
    check if a .git repo already exist in current working directory
    :param verbose: enables verbose logging
    :return:
    """
    if os.path.isdir(".git"):  # if already a git repo
        if verbose:
            print(f"{current_datetime()}: checking if a git repository already exist in {os.getcwd()}")
        print("This seems to be a git repository.")
        print("Use optional [-f | --force] options to create a tit repo")
        if verbose:
            print("example: tit init --force")
        return True
    else:
        return False


def write_file(path, data):
    """
    Write data bytes to file at given path.
    """
    with open(path, 'wb') as f:
        f.write(data)


def create_repo(verbose: bool = False) -> None:
    """
    creates an empty .tit repo
    :param verbose: enables verbose logging
    :return:
    """
    if verbose:
        print(f"{current_datetime()}: making a empty tit repository in {os.getcwd()}")
    try:
        os.mkdir(os.path.join('.tit'))
        for name in ['objects', 'refs', 'refs/heads']:
            os.mkdir(os.path.join('.tit', name))
        write_file(os.path.join('.tit', 'HEAD'),
                   b'ref: refs/heads/main')
        print("Initialized an empty tit repository")
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

    is_git_repo = check_if_git_repo(verbose=verbose)

    if is_git_repo:
        exit(0)
    else:
        if verbose:
            create_repo(verbose=verbose)
        else:
            create_repo()


if __name__ == "__main__":
    app()
