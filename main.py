def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_of_words = get_word_count(text)
    print(f"{num_of_words} words found in the document")
    print(f"--Begin report of {book_path} ---")
    get_letter_count(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return (len(words))

def get_letter_count(text):
    lowered_string = text.lower()
    character_counts = {}
    for char in lowered_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
        
    return character_counts


main()