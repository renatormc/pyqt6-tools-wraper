import subprocess
from typing import Union
import helpers as hp
from pathlib import Path
from InquirerPy import inquirer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import config

def compile_file(file_):
    print(f"Compilando {file_}")
    hp.compile(file_)

def build():
    folder = Path(".")
    items = hp.find_ui_files(folder)
    for item in items:
        compile_file(item)


def get_ui_file(path: Path) -> Union[Path, None]:
    if path.is_dir() and path.name != '.venv':
        for entry in path.iterdir():
            if entry.suffix == ".ui":
                return entry
    elif path.suffix == ".ui":
        return path
    return None


def designer(term):

    if not term:
        subprocess.Popen([config.local_config['designer_exe']])
        return
    path = Path(term)
    file = get_ui_file(path)
    if file:
        subprocess.Popen([config.local_config["designer_exe"], str(file)])
    else:
        folder = Path(".")
        items = hp.find_ui_files(folder, term_search=term)
        if not items:
            print("Item not found")
            return
        file_ = inquirer.select(
            message="Model:",
            choices=items,
        ).execute()
        subprocess.Popen([config.local_config["designer_exe"], file_])


def new_item(item, name):
    if item == "QMainWindow":
        hp.new_main_window(name)
    elif item == "QDialog":
        hp.new_dialog_window(name)
    elif item == "QWidget":
        hp.new_widget(name)
    elif item == "app":
        hp.new_app(name)


class EventHandler(FileSystemEventHandler):
   
    # def on_moved(self, event):
    #     pass

    # def on_created(self, event):
    #     pass

    # def on_deleted(self, event):
    #     pass

    def on_modified(self, event):
        if not event.is_directory:
            path_str = event.src_path.split("#")[0]
            path = Path(path_str)
            ui_file = get_ui_file(path)
            if ui_file:
                compile_file(ui_file)
            

def start_watching(folder, recursive: bool):
    build()
    print("Whatching file changes")
    events = EventHandler()
    observer = Observer()
    observer.schedule(events, folder, recursive=recursive)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.unschedule(events)
        observer.stop()
    observer.join()
