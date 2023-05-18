#stretch challange for week 8
#Let the user input a number nth, then capitalize every letter in the nth position in the string 

quote = "In the comming days, it will not be possible to survive spiritually without the guiding, directing,comforting and constant influence of the Holy Ghost."

run_again = "yes"

while run_again.lower() in ("Yes","yes","YES"):
    favourite_num = int(input("Enter a favourite number: "))
   
    for i, letter in enumerate(quote):
        if i % favourite_num == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    
    run_again = input("Would you like to enter another number? :")
print("goodbye")
