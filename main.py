import sys
from stats import get_num_words, get_char_stats, get_sorted_list_of_dicts


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_stats = get_char_stats(text)
    sorted_list_of_dicts = get_sorted_list_of_dicts(char_stats)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for stat_dict in sorted_list_of_dicts:
        print(f"{stat_dict["char"]}: {stat_dict["num"]}")
    print("============= END ===============")

main()