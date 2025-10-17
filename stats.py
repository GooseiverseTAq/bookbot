import sys
def main():
    path = sys.argv[1]
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    get_report(chars_dict)
    print("============= END ===============")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
