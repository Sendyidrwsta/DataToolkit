from tools import file_tools as ft

def run_file_menu():
    while True:

        print("""
=================
    FILE TOOLS
=================\n
        """)
        file_path = input("Masukkan path file: ")
        info = ft.get_file_info(file_path)

        if info["exists"]:
            print("✅ File ditemukan!")
            print(f"Nama File      : {info['name']}")
            print(f"Ekstensi       : {info['extension']}")
            print(f"Path Absolut   : {info['absolute_path']}")

         
            analysis = ft.get_file_analysis(file_path)
            print("\n--- File Analysis ---")
            print(f"Jumlah Baris   : {analysis['line_count']}")
            print(f"Jumlah Kata    : {analysis['word_count']}")
            print(f"Ukuran File    : {analysis['file_size']} byte")

        else:
            print("❌ File tidak ada atau bukan file.")

        # pilihan setelah selesai
        while True:
            print("""
=================
MENU FILE SELESAI
=================\n
        """)
            print("1. Ulangi File Menu")
            print("0. Kembali ke Main Menu")

            next_choice = input("Pilih : ")
            if next_choice == "1":
                break       # ulangi file_menu (loop luar tetap jalan)
            elif next_choice == "0":
                return      # keluar dari run_file_menu, balik ke main_menu
            else:
                print("Pilihan tidak valid, coba lagi.\n")
