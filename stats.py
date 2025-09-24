# returns the number of words that are in the book
def get_num_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_as_string = f.read()
    words = []
    words = file_as_string.split()
    return len(words)

def text_to_character_count(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_as_string = f.read()

    # process the string into 
    file_as_string = file_as_string.lower()
    letter_dict = {}
    for ch in file_as_string:
            if ch in letter_dict:
                letter_dict[ch] += 1
            else:
                letter_dict[ch] = 1

    return letter_dict


def sort_on(items):
     return items["ch"]

