import os, sys, json, logging, pathlib, yaml
from typing import Any, Dict

def get_logger(name: str = "crime-ml", level=logging.INFO) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    return logging.getLogger(name)

def load_config(path: str = "config.yaml") -> Dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure_dirs(*paths):
    for p in paths:
        pathlib.Path(p).parent.mkdir(parents=True, exist_ok=True)

def save_json(obj: Dict[str, Any], path: str):
    ensure_dirs(path)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def file_exists(path: str) -> bool:
    return pathlib.Path(path).exists()
