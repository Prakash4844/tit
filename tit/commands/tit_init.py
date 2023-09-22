# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit init
# date: 20 Aug, 2023

import os
import typer
from sys import exit
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
        print(f"{current_datetime()}: making a empty tit repository in {os.getcwd()}")
    try:
        os.mkdir(os.path.join('.tit'))
        os.chdir('./.tit')
        tit_dir = os.getcwd()
        for name in ['branches', 'info', 'objects/info', 'objects/pack', 'refs/heads', 'refs/tags']:
            os.makedirs(os.path.join(tit_dir, name), exist_ok=True)

        if verbose:
            print(f"{current_datetime()}: Creating HEAD reference now")
        # Create HEAD reference
        write_binary_file(os.path.join(tit_dir, 'HEAD'),
                          b'ref: refs/heads/main')

        # Create the description file
        with open(os.path.join(tit_dir, 'description'), 'w') as description_file:
            description_file.write("Unnamed repository; edit this file 'description' to name the repository..\n")

        # Create the config file with default settings
        with open(os.path.join(tit_dir, 'config'), 'w') as config_file:
            config_file.write('[core]\n')
            config_file.write('\trepositoryformatversion = 0\n')
            config_file.write('\tfilemode = true\n')
            config_file.write('\tbare = false\n')
            config_file.write('\tlogallrefupdates = true\n')

        if verbose:
            print(f"{current_datetime()}: Creating Index")
        # Initialize an empty index file
        open(os.path.join(tit_dir, 'index'), 'w').close()

        if verbose:
            print(f"{current_datetime()}: Checking out main branch")
        # Initialize an empty main branch
        open(os.path.join(tit_dir, 'refs', 'heads', 'main'), 'w').close()

        if verbose:
            print(f"{current_datetime()}", end=": ")
        print(f"Initialized an empty tit repository in {os.getcwd()}")
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
        exit(0)

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
