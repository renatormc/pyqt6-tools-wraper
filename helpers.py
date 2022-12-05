from pathlib import Path
import subprocess
from typing import List
import config
import shutil
from stringcase import pascalcase, snakecase

def compile(path):
    path = Path(path)
    output = path.parent / f"{path.stem}_ui.py"
    # args = ["python", "-m", "PyQt6.uic.pyuic", str(path), "-o", str(output)]
    args = ["pyuic6", str(path), "-o", str(output)]
    subprocess.run(args)


def find_ui_files(folder: Path, depth=0, term_search="") -> List[Path]:
    if depth >= config.max_depth or folder.name == ".venv":
        return []
    items = []
    for entry in folder.iterdir():
        if entry.is_dir():
            items += find_ui_files(entry, depth + 1, term_search=term_search)
        elif entry.suffix == ".ui":
            if term_search != "" and term_search not in entry.name:
                continue
            items.append(entry)
    return items


def copy_replacing(source, dest, context = {}):
    spath, dpath = Path(source), Path(dest)
    text = spath.read_text(encoding="utf-8")
    for key, value in context.items():
        text = text.replace(f"{{{{ {key} }}}}", value)
    dpath.write_text(text, encoding="utf-8")


def new_main_window(name: str, pfolder="."):
    name_pascal_case, name_snake_case = pascalcase(name), snakecase(name)
    folder = config.app_dir / "files/main_window"
    dest_folder = Path(pfolder) / name_snake_case
    dest_folder.mkdir(parents=True)

    
    context = {'main_window_module': f"{name_snake_case}_ui", 'widget_name': name_pascal_case}
    copy_replacing(folder / "__init__.py", dest_folder / "__init__.py", context)

    context = {'obj_name': name_pascal_case, 'window_title': name_pascal_case}
    copy_replacing(folder / "gui.ui", dest_folder / f"{ name_snake_case }.ui", context)


def new_dialog_window(name: str, pfolder="."):
    name_pascal_case, name_snake_case = pascalcase(name), snakecase(name)
    folder = config.app_dir / "files/dialog_window"
    dest_folder = Path(pfolder) / name_snake_case
    dest_folder.mkdir(parents=True)

    
    context = {'main_window_module': f"{name_snake_case}_ui", 'widget_name': name_pascal_case}
    copy_replacing(folder / "__init__.py", dest_folder / "__init__.py", context)

    context = {'obj_name': name_pascal_case, 'window_title': name_pascal_case}
    copy_replacing(folder / "gui.ui", dest_folder / f"{ name_snake_case }.ui", context)


def new_widget(name: str, pfolder="."):
    name_pascal_case, name_snake_case = pascalcase(name), snakecase(name)
    folder = config.app_dir / "files/widget"
    dest_folder = Path(pfolder) / name_snake_case
    dest_folder.mkdir(parents=True)

    
    context = {'main_window_module': f"{name_snake_case}_ui", 'widget_name': name_pascal_case}
    copy_replacing(folder / "__init__.py", dest_folder / "__init__.py", context)

    context = {'obj_name': name_pascal_case, 'window_title': name_pascal_case}
    copy_replacing(folder / "gui.ui", dest_folder / f"{ name_snake_case }.ui", context)


def new_app(name: str):
    folder = Path(".") / name
    folder.mkdir()
    shutil.copy(config.app_dir / "files/main.py", folder / "main.py")
    shutil.copy(config.app_dir / "files/config.py", folder / "config.py")
    shutil.copy(config.app_dir / "files/helpers.py", folder / "helpers.py")
    new_main_window("MainWindow", folder)

