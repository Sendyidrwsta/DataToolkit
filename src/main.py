from menus.text_menu import run_text_menu
from tools import file_tools as ft

def main():
    print("=== DataToolkit ===")
    # run_text_menu()

    file_path = input("Masukkan path file: ")
    info = ft.get_file_info(file_path)

    if info["exists"]:
        print("✅ File ditemukan!")
        print("Nama file:", info["name"])
        print("Ekstensi file:", info["extension"])
        print("Path absolut:", info["absolute_path"])
    else:
        print("❌ File tidak ada atau bukan file.")


if __name__ == "__main__":
    main()