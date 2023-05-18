#Practice Opening Files

with open("books.txt") as books_list:
    for books in books_list:
        books = books.strip()
        print(books)
        
        
