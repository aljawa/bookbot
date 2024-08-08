def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(get_char_counts(text))

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

main()