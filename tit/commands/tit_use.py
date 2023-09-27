# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit use
# date: 30 Aug, 2023

from typer import Typer
from rich import print
from tit.write_file import write_file, read_tit_config_yaml_file

# create a typer app using required data.
app = Typer(
    help="tit use: Set tit to use a repository that is not of type TIT (eg: git)",
    context_settings={"help_option_names": ["-h", "--help"]}
)


@app.callback(invoke_without_command=True)
def tit_use(vcs: str) -> None:
    """
    tit use: Set tit to use a repository that is not of type TIT (eg: .git)
    :param: vcs (VCS Repo Type (eg: git)
    :return:
    """
    if vcs.lower() == "git":
        if read_tit_config_yaml_file(".git/tit_config.yaml"):
            print("Already set up to use git repo")
        else:
            try:
                write_file(".git/tit_config.yaml", 'Repo_type: ".git"')
                print("[green]Setup:[/green] tit to use .git repository")
            except FileNotFoundError:
                print("[bold red]FATAL:[/bold red] No git repo found.")

    else:
        print(f"[bold red]INVALID:[/bold red] {vcs} VCS not supported.")


if __name__ == "__main__":
    app()
