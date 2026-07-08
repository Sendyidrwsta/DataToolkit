from tools import text_tools as tt  

def run_text_menu():

    text_input = input("Masukkan text : ")
    print(f"Teks yang anda masukkan : {text_input}")

    character_count = tt.count_characters(text_input)
    print(f"Jumlah Karakter: {character_count}")
    word_list = tt.count_words(text_input)
    print(f"Jumlah Kata: {word_list}")

    print()
    print("=== Manipulasi Huruf ===")

    upper_text = tt.to_upper(text_input)
    lower_text = tt.to_lower(text_input)
    title_text = tt.to_title(text_input)

    print(f"Upper : {upper_text}")
    print(f"Lower : {lower_text}")
    print(f"Title : {title_text}")

    text_reverse = tt.reverse_text(text_input)
    print(f"Reversed: {text_reverse}")

    print()
    print("=== Find & Replace ===p")

    find_word = input("Cari   : ")
    replace_word = input("Ganti  : ")
    result = tt.find_and_replace(text_input, find_word, replace_word)
    print(f"Hasil  : {result}")

    print("=== Remove Duplicate Line ===")
    print()

    input_text_multi = tt.input_multiline()
    result_multi = tt.remove_duplicate_lines_from_text(input_text_multi)
    print(f"Hasil : \n{result_multi}")

    # menu sort
    print("=== Sort Lines ===")
    print("1. Ascending")
    print("2. Descending")

    while True:
        choice = input("Pilih : ")
        if choice in ["1", "2"]:
            break
        print("Pilihan tidak valid, coba lagi.\n")

    text_to_sort = result_multi

    if choice == "1":
        result_sort = tt.sort_lines(text_to_sort, reverse=False)
    else:
        result_sort = tt.sort_lines(text_to_sort, reverse=True)

    print("\n=== Hasil ===")
    print(result_sort)
