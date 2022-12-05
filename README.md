# pyqt6-tools-wrapper

Facilitates the creation of pyqt6 applications using QtDesigner.

## Start a new app

```bash
python main.py new app myApp
```

## Watch the ui files changes

If you let this command running in background the .ui files and whenever they change the pyuic will be called to convert it to python code.

```bash
python main.py watch
```

## Create a new QMainWindow

```bash
python main.py new QMainWindow MyWindow
```

## Create a new QDialog

```bash
python main.py new QDialog MyDialog
```

## Create a new QWidget

```bash
python main.py new QWidget MyWidget
```

