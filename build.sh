pyinstaller --noconfirm --onedir --console \
    --icon "./img/Logo/ICO/tit_logo.ico" \
    --name "tit" \
    --add-data "./.venv/lib/python3.11/site-packages/typer:typer/" \
    --add-data "./.venv/lib/python3.11/site-packages/click:click/" \
    --add-data "./.venv/lib/python3.11/site-packages/rich:rich/" \
    --add-data "./.venv/lib/python3.11/site-packages/shellingham:shellingham/" \
    --paths "./.venv/lib/python3.11/site-packages" \
    "./main.py"
