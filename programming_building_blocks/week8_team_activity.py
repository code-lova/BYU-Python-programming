#iterating through 

word = "Committment"
favourite_letter = input("Enter your favourite letter: ")

for letter in word:
    if letter.lower() == favourite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")

print()
print()

for letter in word:
    if letter.lower() == favourite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")