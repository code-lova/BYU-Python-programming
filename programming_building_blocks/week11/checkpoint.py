#Practice Opening Files

with open("books.txt") as books_list:
    for books in books_list:
        books = books.strip()
        print(books)
        
        
with open("book.txt") as manybook:
    for books in manybook:
        print(books)