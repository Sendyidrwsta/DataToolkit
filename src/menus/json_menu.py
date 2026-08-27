from tools import json_tools as jt


def run_json_menu():
    while True:
        print("""
=================
    JSON TOOLS
=================\n
1. JSON Formatter
0. Back
        """)

        choice_json_menus = input("Pilih : ")

        if choice_json_menus == "1":
            file_path = input("Masukkan nama file JSON: ")
            data = jt.read_json(file_path)

            if data is None:
                print("❌ File tidak ditemukan atau format JSON salah.")
            else:
                print("\n--- Isi File JSON ---")
                print(jt.format_json(data))

        elif choice_json_menus == "0":
            return

        else:
            print("❌ Pilihan tidak valid, coba lagi.")
            continue

        # === Post-menu setelah selesai ===
        while True:
            print("""
=================
JSON TOOLS SELESAI
=================\n
1. Ulangi JSON Tools
2. Kembali ke Main Menu
            """)

            next_choice = input("Pilih : ")

            if next_choice == "1":
                break
            elif next_choice == "2":
                return
            else:
                print("Pilihan tidak valid, coba lagi.\n")