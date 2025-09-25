from stats import text_to_character_count, get_num_words, to_report_list, sort_on
import sys

'''
def get_book_text(filepath):
    # use with to open
    # f is the filepath
    with open(filepath, 'r', encoding='utf-8') as f:\
        file_as_string = f.read()
    return file_as_string
'''

def print_report(filepath):
    results = to_report_list(text_to_character_count(filepath))
    num_words = get_num_words(filepath)
    results.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ea in results:
        print(f"{ea['char']}: {ea['num']}")
    print("============= END ===============")
    return None


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # use the relative filepath of the book to get the contents
    ## print(text_to_character_count('./books/frankenstein.txt'))
    ## print(to_report_list(text_to_character_count('./books/frankenstein.txt')).sort(reverse=True,key=sort_on))

    print_report(sys.argv[1])
    sys.exit(0)
main()
