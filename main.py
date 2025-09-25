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

def print_report(results):
    num_words = get_num_words('./books/frankenstein.txt')
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ea in results:
        print(f"{ea['char']}: {ea['num']}")
    print("============= END ===============")
    return None


def main():
    # use the relative filepath of the book to get the contents
    ## print(text_to_character_count('./books/frankenstein.txt'))
    ## print(to_report_list(text_to_character_count('./books/frankenstein.txt')).sort(reverse=True,key=sort_on))
    results = to_report_list(text_to_character_count('./books/frankenstein.txt'))
    results.sort(reverse=True, key=sort_on)
    print_report(results)
main()
