from pathlib import Path
import os
import subprocess
import stat

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))

def get_poetry_venv():
    text = subprocess.getoutput("poetry env info")
    lines = text.split("\n")
    for line in lines:
        if line.startswith("Path: "):
            return Path(line.replace("Path: ", "").strip())
    raise Exception("Executable not found")

python_folder = get_poetry_venv()
activate = python_folder / "Scripts/activate.bat" 

p = app_dir / "main.py"
folder = input("Destination folder: ")

if os.name == "windows":
    activate = python_folder / "Scripts/activate.bat"
    p2 = Path(folder) / "p6w.bat"
    text = f"""@echo off
    "{activate}"
    python \"{p}\" %*
    """
    p2.write_text(text)
else:
    activate = python_folder / "bin/activate"
    p2 = Path(folder) / "p6w"
    text = f"""#!/bin/bash
    source \"{activate}\"
    python \"{p}\" $@
    """
    p2.write_text(text)
    st = os.stat(p2)
    os.chmod(p2, st.st_mode | stat.S_IEXEC)