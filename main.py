from stats import word_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(f"{book_path}")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

#function to open selected book and provide it's contents as a string
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        return f.read()

main()