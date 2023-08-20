# authors: ["Prakash4844 <pk484442@gmail.com>"]
# command: tit init
# date: 20 Aug, 2023

import os
from typer import Typer

app = Typer(help="tit init: Create an empty Tit repository or reinitialize an existing one")


@app.callback(invoke_without_command=True)
def tit_init():
    """
    tit init: Create an empty Tit repository or reinitialize an existing one.
    :return:
    """
    create_repo = True
    if os.path.isdir(".git"):  # if already a git repo
        print("this seems to be a git repository.")
        print("are you sure you want to create a tit repository here?(y/n)")
        create_tit_repo = input().lower()

        if create_tit_repo == 'y' or create_tit_repo == 'yes':
            pass
        else:
            create_repo = False

        if not create_repo:
            print("didn't Initialize a tit repo")
        else:
            try:
                os.mkdir(".tit")
                print("Initialized an empty tit repository")
            except FileExistsError:
                print("a tit repo already exist.")


if __name__ == "__main__":
    app()
