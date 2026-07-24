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

def merge_csv(file1: str, file2: str, output_file: str) -> bool:
    """
    Menggabungkan dua file CSV dengan aturan:
    - Kedua file harus memiliki header yang sama.
    - Jika header berbeda, fungsi mengembalikan False.
    - Header pada file kedua tidak ikut ditulis lagi.
    - Output file otomatis diberi ekstensi .csv jika belum ada.
    """
    # pastikan output_file berakhiran .csv
    if not output_file.lower().endswith(".csv"):
        output_file += ".csv"

    data1 = read_csv(file1)
    data2 = read_csv(file2)

    if not data1 or not data2:
        return False

    header1 = get_headers_from_data(data1)
    header2 = get_headers_from_data(data2)

    if header1 != header2:
        return False

    # gabungkan data (tanpa header kedua)
    merged_data = [header1] + data1[1:] + data2[1:]

    try:
        with open(output_file, "w", encoding="utf-8", newline="") as fout:
            writer = csv.writer(fout)
            writer.writerows(merged_data)
        return True
    except (FileNotFoundError, OSError):
        return False
 

