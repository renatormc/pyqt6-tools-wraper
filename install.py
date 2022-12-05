from pathlib import Path
import os

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))

python = app_dir / ".venv\\Scripts\\python.exe"
p = app_dir / "main.py"
folder = input("Destination folder: ")
p2 = Path(folder) / "p6w.bat"

text = f"""@echo off
\"{python}\" \"{p}\" %*
"""
p2.write_text(text)