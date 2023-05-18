#Still on file opening lists, and if else statement
#practice finding items in a file

books_list = []
chapters_list = []
testament_list = []


with open("books_and_chapters.txt") as bible_file:
    for eachline in bible_file:
        parts = eachline.split(":")   
        
        books = str(parts[0].strip())
        chapters = int(parts[1].strip())
        testament = str(parts[2].strip())
        
        #print(chapters)
        
        books_list.append(books)
        chapters_list.append(chapters)
        testament_list.append(testament)
        
        #print(testament_list)
        
    max_chapter = -1
    books_with_max = ""
    
    for i, verse in enumerate(chapters_list):
        book_name = books_list[i]
        if verse > max_chapter:
            max_chapter = verse
            books_with_max = book_name
    
print()
print("Scripture:{}, Books: {}, Chapters: {}".format(testament, books, chapters))
print()
print("The largest chapter in the scripture is: {} in the books of {}".format(max_chapter, books_with_max))
print()
    
    

#Stretch Challange to print only the books in the 
#Books of mormon

new_books_of_mormon = []
book_of_mormon = []
mormon_books = "" 
max_moromon_books = -1
mormon_books_max = "" 


for j, each_mormon in enumerate(testament_list):
    maximum_mormon = chapters_list[j]
    if each_mormon.lower() == "book of mormon":
        books_in_mormon = books_list[j] #Assigning all books in "book of mormon" to a varable called books_in_mormon
        mormon_books = books_in_mormon 
        new_books_of_mormon.append(mormon_books) #Appending the books to a list   

        if maximum_mormon > max_moromon_books:
            max_moromon_books = maximum_mormon
            mormon_books_max = books_in_mormon
        
  

print("The Books in the Book of Mormon are listed below:")
print(new_books_of_mormon) 

print("The largest book in the book of mormon is: '{}' with chapter '{}'".format(mormon_books_max, max_moromon_books))


print()

max_vol = -1
max_volme_name = ""
volume_list = []
vmn = ""
invalid = "No books or scripture found.."


print("What volume of the scripture would you like to learn about? ", end="")
volume = str(input(""))
volume = volume.lower()
for v, each_volume in enumerate(testament_list):
    each_volume = each_volume.lower()
    maximum_volume = chapters_list[v]
    maximum_volume_book = books_list[v] 
    
    if each_volume == volume:
        vmn = each_volume.title()
        if maximum_volume > max_vol:
            max_vol = maximum_volume
            max_volme_name = maximum_volume_book
    
        
print()
print("The maximum volum of books in the {} is {} in the book of {}".format(vmn, max_vol, max_volme_name))
print()

