def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_of_words = get_word_count(text)
    print(f"{num_of_words} words found in the document")
    print(f"--Begin report of {book_path} ---")
    char_dictionary = get_letter_count(text)
    sorted_char_list = print_out_char_counts(char_dictionary)
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['number']} times")
    print("--- End report ---")

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

def sort_on(d):
    return d["number"]

def print_out_char_counts(char_counts_dict):
    list_of_dicts = []
    for char in char_counts_dict:
        list_of_dicts.append({"char": char, "number": char_counts_dict[char]}) 
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

main()