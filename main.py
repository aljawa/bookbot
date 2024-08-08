def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_char_counts(text)
    sorted_chars = get_sorted_list(chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    lowered = text.lower()
    chars = {}
    
    for char in lowered:
        if char not in chars.keys():
            chars[char] = 1
        else: 
            chars[char] += 1
    return chars

def sort_on(d):
    return d["num"]

def get_sorted_list(d):
    sorted_list = []
    for char in d:
        sorted_list.append({"char": char, "num": d[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()