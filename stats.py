#function to count words in a given string
def word_count(book_contents):
    words = book_contents.split()
    return len(words)

#function to take text from the book as a string and returns the number of times each character, (iincluding symbols and spaces), appears in the string.
def character_count(book_text):
    lowercase_text = book_text.lower()
    character_dict = {
        
    }
    for character in lowercase_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    
    return character_dict

def dict_sort_helper(char_dict):
    return char_dict["num"]
    
def sort_dict(char_dict):
    char_dict_list = []

    for char in char_dict:
        count = char_dict[char]
        char_dict_list.append({
            "char": char,
            "num": count,
        })
    char_dict_list.sort(reverse=True, key=dict_sort_helper)
    
    return char_dict_list