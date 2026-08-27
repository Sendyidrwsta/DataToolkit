import json

def read_json(file_path: str) -> dict | list | None:
    "Membacara file JSON"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return None

def write_json(file_path: str, data: dict | list) -> bool:
    "Menulis Ulang JSON"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except (OSError, TypeError):
        return False

def format_json(data: dict | list) -> str:
    "Memformat file Json dengan Indent/spasi 4"
    return json.dumps(data, indent=4, ensure_ascii=False)