import json
from pathlib import Path


JSON_FILE = Path(__file__).resolve().parent.parent / 'operations.json'


def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

def list(glos):
    for glo in glos:
        if glo['date'] is not None:
            print(f"{glo['date']}")


list(load_json(JSON_FILE))
