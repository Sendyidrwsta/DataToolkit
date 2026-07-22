from tools import csv_tools as ct

def run_csv_menu():
    while True:

        print("""
=================
    CSV TOOLS
=================\n
        """)
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

        # pilihan setelah selesai
        while True:
            print("""
=================
MENU CSV SELESAI
=================\n
        """)
            print("1. Ulangi CSV Menu")
            print("0. Kembali ke Main Menu")

            next_choice = input("Pilih : ")
            if next_choice == "1":
                break       # ulangi csv_menu (loop luar tetap jalan)
            elif next_choice == "0":
                return      # keluar dari run_csv_menu, balik ke main_menu
            else:
                print("Pilihan tidak valid, coba lagi.\n")
