# returns the number of words that are in the book
def get_num_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_as_string = f.read()
    words = []
    words = file_as_string.split()
    return len(words)

## returns a dict of the {letter, num}
def text_to_character_count(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_as_string = f.read()

    # process the string into 
    text = file_as_string.lower()
    counts = {}
    for ch in text:
        if not ch.isalpha():
            continue
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def to_report_list(counts):
    result = []
    for ch, num in counts.items():
        result.append({"char": ch, "num": num})
    return result

def sort_on(items):
    return items["num"]
