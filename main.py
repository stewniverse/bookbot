from stats import get_num_words
from stats import text_to_character_count

'''
def get_book_text(filepath):
    # use with to open
    # f is the filepath
    with open(filepath, 'r', encoding='utf-8') as f:\
        file_as_string = f.read()
    return file_as_string
'''
def main():
    # use the relative filepath of the book to get the contents
    num_words = get_num_words('./books/frankenstein.txt')
    print(f"Found {num_words} total words")

    print(text_to_character_count('./books/frankenstein.txt'))

main()
