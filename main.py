from stats import get_num_words, get_num_char, get_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    word_count = get_num_char(book_text)
    sorted_count = get_sorted_list(word_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count_dict in sorted_count:
        if count_dict["char"].isalpha():
            print(f"{count_dict["char"]}: {count_dict["num"]}")
    print("============= END ===============")

main()
