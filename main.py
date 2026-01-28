from stats import word_count, character_count, sort_dict

def main():
    #sets book path and makes book text into a string
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(f"{book_path}")
    
    #Prints headers
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    #sets word count variable and prints it
    num_words = word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #print statement to print the character count dictionary
    print("--------- Character Count -------")
    char_count_dict = character_count(book_text)
    #print(f"Character count is {char_count_dict}")

    #calls sort dict function from stats and stores it in variable "sorted_dict"
    sorted_dict = sort_dict(char_count_dict)
    #iterates through the sorted list checking if the character in the sorted dict is alphanumeric, prints key,value pair if true.
    for item in sorted_dict:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    
    #print END
    print("============= END ===============")

#function to open selected book and provide it's contents as a string
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        return f.read()

main()