from tools import csv_tools as ct

def run_csv_menu():
    while True:
        print("""
=================
    CSV TOOLS
=================\n
1. CSV Analyzer
2. Merge CSV
3. Split CSV
4. Remove Duplicates
5. SEARCH DATA 
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

            merged = ct.merge_csv_data(file1, file2)
            if merged:
                ct.write_csv(output_file, merged)
                print("\n✅ Berhasil menggabungkan file.")
            else:
                print("\n❌ Gagal: header tidak cocok atau file error.")

        elif choice_csv_menus == "3":
            source_file = input("Masukkan path CSV: ")
            try:
                rows_per_file = int(input("Jumlah baris per file: "))
            except ValueError:
                print("\n❌ Jumlah baris harus berupa angka.")
                continue
            output_prefix = input("Prefix file output (tanpa .csv): ")

            result_split = ct.split_csv(source_file, rows_per_file, output_prefix)
            if result_split:
                print("\n✅ Berhasil membagi file CSV.")
            else:
                print("\n❌ Gagal membagi file CSV.")

        elif choice_csv_menus == "4":
            source_file = input("Masukkan path CSV: ")
            output_file = input("Masukkan nama/path file hasil: ")

            data = ct.read_csv(source_file)
            if data:
                clean = ct.remove_duplicate_rows(data)
                if ct.write_csv(output_file, clean):
                    print("\n✅ Berhasil menghapus duplikat dan menyimpan file.")
                else:
                    print("\n❌ Gagal menulis file hasil.")
            else:
                print("\n❌ File tidak ada atau bukan file CSV.")

        elif choice_csv_menus == "5":
            source_file = input("Masukkan path CSV: ")
            keyword = input("Masukkan Kata Yang ingin Dicari: ")

            data = ct.read_csv(source_file)
            if data is None:
                print("File Tidak Ada Atau File Bukan CSV")
            else:
                result_search = ct.search_data(data, keyword)
                if len(result_search) > 1:
                    for row in result_search:
                        print(", ".join(row))
                else:
                    print("Tidak Ada Hasil Yang Ditemukan")
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
