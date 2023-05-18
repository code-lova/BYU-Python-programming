# There are two types of loops in python
#1 is the for loop and 
#2 is the while loop

#example 
people = ['matter','hanna']

for name in people:
    print(name)

#This loop will start will 0 and go up to 20 but not include 20 in the count.
for index in range(0, 20):
    print(index)
    
#This loop does same but will start will 0 and go up to 20 and will count in 2's.
for index in range(0, 20, 2):
    print(index)
    
#lets check another example where we use while loop 

people = ['matter','hanna']
index = 0
while index < len(people):
    print(people[index])
    index += 1
    
#Lets do a loop in another loop
for i in range(1,5):
    #print(i)
    for j in range(10, 13):
        print("{}--{}".format(i,j))
        
# This loop prints out each lettter in the first_name variable as it loops       
first_name = "EBIZO"
for letter in first_name:
    print("the letter is {}".format(letter))
    
#getting the position of a letter in a string
second_name = "EBIZO"
fouth_letter = second_name[4]
print(fouth_letter)

#iterating through each letter using index, by index we mean what is the lenght of the variable
word = "book"
number_of_letters = len(word)
for index in range(number_of_letters):
    print(index)
    
#we can use square brackets to also access the letter at that index as follows
word = "book"
number_of_letters = len(word)
for index in range(number_of_letters):
    letter = word[index]
    print("index:{} letter: {}".format(index, letter))

#We can also use enumerate function in getting the index and letter in a string
word = "book"
for i, letter in enumerate(word, start=1):
    print("The position {} is for the letter {}".format(i, letter))