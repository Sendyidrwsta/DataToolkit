from menus.main_menu import run_main_menu
from menus.file_menu import run_file_menu
from menus.text_menu import run_text_menu

def main():
    while True:
        pilihan = run_main_menu()

        if pilihan == "1":
            run_text_menu()
        elif pilihan == "2":
            run_file_menu()
        elif pilihan == "0":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()