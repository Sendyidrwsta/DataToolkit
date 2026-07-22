import csv

def read_csv(file_path: str) -> list[list[str]] | None:
    """
    Membaca seluruh isi CSV sekali saja.
    Mengembalikan list of rows (list of list of str).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    except (FileNotFoundError, OSError):
        return None

def preview_from_data(data: list[list[str]], n: int = 5) -> list[list[str]]:
    """
    Mengembalikan header beserta n baris data pertama.
    """
    return data[:n+1] if data else []

def get_headers_from_data(data: list[list[str]]) -> list[str]:
    """
    Mengambil header (nama kolom) dari data CSV.
    """
    return data[0] if data else []


def count_rows_from_data(data: list[list[str]]) -> int:
    """Menghitung jumlah baris data (tanpa header)."""
    return len(data) - 1 if data else 0

def count_columns_from_data(data: list[list[str]]) -> int:
    """Menghitung jumlah kolom dari header."""
    return len(data[0]) if data else 0

def get_csv_summary_from_data(data: list[list[str]]) -> dict:
    """
    Ringkasan CSV dari data yang sudah dibaca:
    - row_count: jumlah baris data (tanpa header)
    - column_count: jumlah kolom
    """
    if not data:
        return {"row_count": None, "column_count": None}

    return {
        "row_count": count_rows_from_data(data),
        "column_count": count_columns_from_data(data)
    }

