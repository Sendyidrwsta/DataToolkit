from tools import csv_tools as ct

def run_csv_menu():
    while True:
        print("""
=================
    CSV TOOLS
=================\n
1. CSV Analyzer
2. Merge CSV
0. Back
        """)
        choice_csv_menus = input("Pilih : ")

        if choice_csv_menus == "1":
            file_path = input("Masukkan path CSV: ")
            data = ct.read_csv(file_path)

            if data is not None:
                print("✅ File CSV ditemukan!")

                # tampilkan summary
                summary = ct.get_csv_summary_from_data(data)
                print("\n--- CSV Summary ---")
                print(f"Jumlah Baris   : {summary['row_count']}")
                print(f"Jumlah Kolom   : {summary['column_count']}")

                # tampilkan headers
                headers = ct.get_headers_from_data(data)
                print("\n--- Headers ---")
                print(", ".join(headers))

                # tampilkan preview
                preview = ct.preview_from_data(data, n=5)
                print("\n--- Preview ---")
                for row in preview:
                    print(", ".join(row))
            else:
                print("❌ File tidak ada atau bukan file CSV.")

        elif choice_csv_menus == "2":
            file1 = input("Masukkan path CSV pertama : ")
            file2 = input("Masukkan path CSV kedua   : ")
            output_file = input("Masukkan nama/path file hasil : ")

            result = ct.merge_csv(file1, file2, output_file)

            if result:
                print("\n✅ Berhasil menggabungkan file.")
            else:
                print("\n❌ Gagal: header tidak cocok atau file error.")

        elif choice_csv_menus == "0":
            return    # keluar ke main_menu

        # === Post-menu setelah selesai ===
        while True:
            print("""
=================
CSV TOOLS SELESAI 
=================\n
1. Ulangi CSV Tools
2. Kembali ke Main Menu
            """)
            next_choice = input("Pilih : ")
            if next_choice == "1":
                break       # ulangi run_csv_menu (loop luar tetap jalan)
            elif next_choice == "2":
                return      # keluar ke main_menu
            else:
                print("Pilihan tidak valid, coba lagi.\n")
