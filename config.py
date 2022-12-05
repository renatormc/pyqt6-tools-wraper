from pathlib import Path
import os
import json
from typing import TypedDict

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))

max_depth = 3

class LocalConfigType(TypedDict):
    designer_exe: str

with (app_dir / "config.json").open("r", encoding="utf-8") as f:
    local_config: LocalConfigType = json.load(f)
    