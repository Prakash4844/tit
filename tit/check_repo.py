# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: N/A
# date: 31 Aug, 2023

import os
import datetime
import yaml
from rich import print


def current_datetime():
    """
    :return: current datetime
    """
    current = datetime.datetime.now()
    formatted_current = current.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_current


def print_info(verbose: bool = False):
    print("This seems to be a git repository, but is not set up to be used with tit.")
    print("Use [bold green]tit use[/bold green] command to set up tit to use already available git "
          "repo.")
    print("Use optional [blue][-f | --force][/blue] options to create a tit repo.\n\n")
    if verbose:
        print("example 1: [bold green]tit init[/bold green] [blue][-f | --force][/blue]\nOR")
        print("example 2: [bold green]tit use git[/bold green]")


def check_if_repo(verbose: bool = False) -> bool:
    """
    check if a .git repo already exist in current working directory
    :param verbose: enables verbose logging
    :return:
    """
    if verbose:
        print(f"{current_datetime()}: checking if a git repository already exist in {os.getcwd()}")

    if os.path.isdir(".tit"):  # if already a tit repo
        if verbose:
            print(f'tit repo found in {os.getcwd()}')
        return True
    else:
        if os.path.isdir(".git"):  # if already a git repo
            try:
                if os.path.isfile('.git/tit_config.yaml'):
                    with open(os.path.join('.git/tit_config.yaml')) as file:
                        tit_config = yaml.safe_load(file)
                        tit_config = dict(tit_config)
                        if tit_config.get('Repo_type') == '.git':
                            print("repo already set up.")
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
        else:
            print(f'[bold red]Error:[/bold red] Neither git nor a tit repo found in {os.getcwd()}')
            return False
