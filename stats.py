#function to count words in a given string
def word_count(book_contents):
    words = book_contents.split()
    return len(words)