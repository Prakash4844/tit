# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 31 Aug, 2023

import os
import datetime
import yaml
from rich import print


def current_datetime():
    """
    Get the current datetime in a formatted string.
    :return: Formatted current datetime string.
    """
    current = datetime.datetime.now()
    formatted_current = current.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_current


def print_info(verbose: bool = False):
    """
    Print information about setting up tit repository.
    :param: verbose: If True, print verbose instructions.
    """
    print("This seems to be a git repository, but is not set up to be used with tit.")
    print("Use [bold green]tit use[/bold green] command to set up tit to use already available git "
          "repo. \n\t\t\tOR")
    print("Use optional [blue][-f | --force][/blue] options to create a tit repo.\n")
    if verbose:
        print("example 1: [bold green]tit init[/bold green] [blue][-f | --force][/blue]\n\t\tOR")
        print("example 2: [bold green]tit use git[/bold green]")


def check_tit_config(verbose: bool = False) -> bool:
    """
    check if the git repo is set up to be used with tit.
    :param verbose: If True, print verbose information.
    :return: bool
    """
    try:
        if os.path.isfile('.git/tit_config.yaml'):
            with open(os.path.join('.git/tit_config.yaml')) as file:
                tit_config = yaml.safe_load(file)
                tit_config = dict(tit_config)
                if tit_config.get('Repo_type') == '.git':
                    print("tit is set up to work with already present git repo.")
                    return True
                else:
                    return False
        else:
            print_info(verbose)
            return True
    except (FileNotFoundError, yaml.YAMLError):
        if yaml.YAMLError:
            print("[bold red]Error:[/bold red] Invalid YAML")
            return True
        print_info(verbose)
        return True


def check_if_repo(verbose: bool = False) -> bool:
    """
    check if a .git repo already exist in current working directory
    Print information about setting up tit repository.
    :param verbose: If True, print verbose  information.
    :returns: bool
    """

    if verbose:
        print(f"{current_datetime()}: checking if a git repository already exist in current or any of the parent "
              f"directories")

    current_dir = os.getcwd()  # Get the current working directory
    while current_dir != "/":  # Stop when reaching the root directory
        if os.path.isdir('.tit'):
            print(f'A tit repo found in "{os.getcwd()}"')
            return True
        elif os.path.isdir('.git'):
            print(f'A git repo found in "{os.getcwd()}"')
            is_config = check_tit_config(verbose)
            return is_config
        current_dir = os.path.dirname(current_dir)  # Move to the parent directory
    if verbose:
        print('[bold red]Error:[/bold red] Neither git nor a tit repo found in current or any of the parent '
              'directories.')
    return False
