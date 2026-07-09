import os

def check_file(file_path: str) -> bool:
    """
    Mengecek apakah file ada di path tertentu.
    Mengembalikan True jika ada, False jika tidak.
    """
    return os.path.isfile(file_path)

def get_file_name(file_path: str) -> str:
    """
    Mengembalikan nama file dari sebuah path.
    """
    return os.path.basename(file_path)

def get_extension(file_path: str) -> str:
    """
    Mengembalikan ekstensi file dari sebuah path.
    Contoh: 'data.txt' -> 'txt'
    """
    return os.path.splitext(file_path)[1].lstrip(".")

def get_absolute_path(file_path: str) -> str:
    """
    Mengembalikan path absolut dari sebuah file.
    """
    return os.path.abspath(file_path)


def get_file_info(file_path: str) -> dict:
    """
    Wrapper untuk menggabungkan semua fungsi file tools.
    """
    info = {
        "exists": check_file(file_path),
        "name": get_file_name(file_path),
        "extension": get_extension(file_path),
        "absolute_path": get_absolute_path(file_path),
    }
    return info