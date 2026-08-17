import csv

# ======================
# Bagian I/O
# ======================

def read_csv(file_path: str) -> list[list[str]] | None:
    """Membaca seluruh isi CSV sekali saja."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    except (FileNotFoundError, OSError):
        return None


def write_csv(file_path: str, data: list[list[str]]) -> bool:
    """Menulis ulang data CSV ke file."""
    if not data:
        return False
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        return True
    except (FileNotFoundError, OSError):
        return False


# ======================
# Bagian Analisis
# ======================

def preview_from_data(data: list[list[str]], n: int = 5) -> list[list[str]]:
    """Mengembalikan header beserta n baris data pertama."""
    return data[:n+1] if data else []


def get_headers_from_data(data: list[list[str]]) -> list[str]:
    """Mengambil header (nama kolom)."""
    return data[0] if data else []


def get_rows_from_data(data: list[list[str]]) -> list[list[str]]:
    """Mengambil semua baris data tanpa header."""
    return data[1:] if data else []


def count_rows_from_data(data: list[list[str]]) -> int:
    """Menghitung jumlah baris data (tanpa header)."""
    return len(data) - 1 if data else 0


def count_columns_from_data(data: list[list[str]]) -> int:
    """Menghitung jumlah kolom dari header."""
    return len(data[0]) if data else 0


def get_csv_summary_from_data(data: list[list[str]]) -> dict:
    """Ringkasan CSV: jumlah baris & kolom."""
    if not data:
        return {"row_count": None, "column_count": None}
    return {
        "row_count": count_rows_from_data(data),
        "column_count": count_columns_from_data(data)
    }

def search_data(data: list[list[str]], keyword: str) -> list[list[str]]:
    """
    Mencari keyword pada seluruh kolom (case-insensitive).
    - data: list of lists (hasil read_csv)
    - keyword: string yang dicari
    - return: list of lists berisi header + baris yang cocok
    """
    if not data or not keyword or keyword.strip() == "":
        return []

    header = data[0]
    keyword_lower = keyword.strip().lower()
    matched_rows = []

    for row in data[1:]:
        # cek apakah ada kolom yang mengandung keyword
        if any(keyword_lower in cell.lower() for cell in row):
            matched_rows.append(row)

    return [header] + matched_rows if matched_rows else []


# ======================
# Bagian Transformasi
# ======================

def merge_csv_data(file1: str, file2: str) -> list[list[str]] | None:
    """Menggabungkan dua file CSV jadi data list (tanpa tulis file)."""
    data1 = read_csv(file1)
    data2 = read_csv(file2)
    if not data1 or not data2:
        return None
    header1 = get_headers_from_data(data1)
    header2 = get_headers_from_data(data2)
    if header1 != header2:
        return None
    return [header1] + get_rows_from_data(data1) + get_rows_from_data(data2)


def split_csv(source_file: str, rows_per_file: int, output_prefix: str = "split") -> bool:
    """Membagi file CSV besar tanpa memuat seluruh isi ke RAM."""
    if rows_per_file <= 0:
        return False
    try:
        with open(source_file, "r", encoding="utf-8") as fin:
            reader = csv.reader(fin)
            try:
                header = next(reader)
            except StopIteration:
                return False
            file_index = 1
            rows_buffer = []
            for row in reader:
                rows_buffer.append(row)
                if len(rows_buffer) == rows_per_file:
                    output_file = f"{output_prefix}_{file_index}.csv"
                    write_csv(output_file, [header] + rows_buffer)
                    file_index += 1
                    rows_buffer = []
            if rows_buffer:
                output_file = f"{output_prefix}_{file_index}.csv"
                write_csv(output_file, [header] + rows_buffer)
        return True
    except (FileNotFoundError, OSError):
        return False

def remove_duplicate_rows(data: list[list[str]]) -> list[list[str]]:
    """Menghapus baris duplikat, header tetap dipertahankan."""
    if not data:
        return []
    header = data[0]
    seen = set()
    unique_rows = []
    for row in data[1:]:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)
    return [header] + unique_rows

def filter_column(data: list[list[str]], column: str, value: str) -> list[list[str]] | None:
    """
    Filter data berdasarkan nama kolom (case-insensitive).
    - None → kolom tidak ditemukan
    - []   → kolom valid, tapi tidak ada data yang cocok
    - list → header + baris yang cocok
    """
    if not data :
        return []

    header = data[0]
    # normalisasi input kolom dan value
    column = column.strip().lower()
    value = value.strip().lower()

    if not column or not value:
        return []

    # cari index kolom
    try:
        col_index = next(i for i, h in enumerate(header) if h.strip().lower() == column)
    except StopIteration:
        return None  # kolom tidak ditemukan

    matched_rows = []
    for row in data[1:]:
        if not row: 
            continue
        # cek panjang row agar tidak IndexError
        if col_index < len(row):
            if row[col_index].strip().lower() == value:
                matched_rows.append(row)

    return [header] + matched_rows if matched_rows else []

