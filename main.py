from stats import word_count, character_count

def main():
    #sets book path and makes book text into a string
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(f"{book_path}")
    
    #sets word count variable and prints it
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

    #print statement to print the character count dictionary
    print(f"Character count is {character_count(book_text)}")

#function to open selected book and provide it's contents as a string
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        return f.read()

main()