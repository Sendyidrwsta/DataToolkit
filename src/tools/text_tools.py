def count_characters (text: str) -> int:
    """Menghitung jumlah Karakter text"""
    return len(text)

def count_words(text: str) -> int:
    """Menghitung jumlah kata dalam text"""
    return len(text.split())

def to_upper(text: str) -> str:
    """Mengubah text menjadi upper"""
    return text.upper()

def to_lower(text: str) -> str:
    """Mengubah text menjadi lower"""
    return text.lower()

def to_title(text: str) -> str:
    """Mengubah text menjadi title"""
    return text.title()

def reverse_text(text: str) -> str:
    """Membalik urutan text"""
    return text[::-1]

def find_and_replace(text: str, find_word: str, replace_word: str) -> str:
    """
    Fungsi untuk mencari dan mengganti teks.
    - text: string sumber
    - find_word: teks yang ingin dicari
    - replace_word: teks pengganti
    """
    return text.replace(find_word, replace_word)


def input_multiline():
    print("Masukkan teks (tekan Enter pada baris kosong untuk selesai):")
    line_text = []
    
    while True:
        inputan = input()
        if inputan == "":
            break
        line_text.append(inputan)
        
    return "\n".join(line_text)

def remove_duplicate_lines_from_text(text: str) -> str:

    """
    Menghapus baris duplikat dari sebuah string teks.
    """
    lines = text.splitlines()   
    unique_lines = []           

    for line in lines:
        if line not in unique_lines:   
            unique_lines.append(line)  

    return "\n".join(unique_lines) 

def sort_lines(text: str, reverse: bool = False) -> str:
    """
    Mengurutkan baris teks dari sebuah string.
    - Default ascending (reverse=False)
    - Jika reverse=True maka descending
    """
    lines = text.splitlines()            
    sorted_lines = sorted(lines, reverse=reverse)  
    return "\n".join(sorted_lines)