from tools import file_tools as ft

def run_file_menu():
    while True:

        print("""
===============
  DATA TOOLKIT
===============\n
        """)
        file_path = input("Masukkan path file: ")
        info = ft.get_file_info(file_path)

        if info["exists"]:
            print("✅ File ditemukan!")
            print("Nama file:", info["name"])
            print("Ekstensi file:", info["extension"])
            print("Path absolut:", info["absolute_path"])
        else:
            print("❌ File tidak ada atau bukan file.")

        # pilihan setelah selesai
        while True:
            print("\n=== Menu File Selesai ===")
            print("1. Ulangi File Menu")
            print("0. Kembali ke Main Menu")

            next_choice = input("Pilih : ")
            if next_choice == "1":
                break       # ulangi file_menu (loop luar tetap jalan)
            elif next_choice == "0":
                return      # keluar dari run_file_menu, balik ke main_menu
            else:
                print("Pilihan tidak valid, coba lagi.\n")
