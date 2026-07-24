
def run_main_menu():
    """
    menampilkan menu utama,
    membaca pilihan pengguna,
    mengembalikan pilihan sebagai string.
    """
    
    print("""
=================
   DATA TOOLKIT
=================\n
1.Text Tools
2.File Tools
3.CSV  Tools
0.EXIT
    """)
    choice = input("Pilih :")
    return choice
