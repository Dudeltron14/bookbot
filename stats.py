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
