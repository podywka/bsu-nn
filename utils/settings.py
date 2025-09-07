from pathlib import Path
from typing import Tuple

_BASE_DIR = Path(__file__).resolve().parent.parent

def get_base_dir():
    print("(!) Make sure this dir is project directory: ", _BASE_DIR)
    return _BASE_DIR

DATA_DIR = _BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

_INPUTS_DIR = DATA_DIR / "inputs"
_OUTPUTS_DIR = DATA_DIR / "outputs"

def get_in_out_dirs(base_name: str) -> Tuple[Path, Path]:
    in_dir = _INPUTS_DIR / base_name
    out_dir = _OUTPUTS_DIR / base_name

    in_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    return in_dir, out_dir
