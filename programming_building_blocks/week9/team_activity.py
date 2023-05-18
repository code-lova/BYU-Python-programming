# A program that ask for numbers as user input
#And add them to a list
#Then sum the numbers
#find the average 
#Find the Largest number
#find the smallest positive number
#And lastly sort the numbers

print("--Enter a list of numbers, press 0 when finished--")
print()
numbers = []

end_prog = 0
new_num = 1
running_sum = 0
empty = ""

while new_num != end_prog:
    new_num = int(input("Enter a Number: "))    
    numbers.append(new_num)
    #finding the sum of all numbers
for numbs in numbers:
    running_sum += numbs
#Finding the average in the list    
length = len(numbers)
total = sum(numbers)
average = length / total
#Finding the largest numbers 
largest = max(numbers)
#Finding the smallest positive number
minumum_num_positive = min(i for i in numbers if i > 0)
#delearing sorting the numbers first 
sort_numbers = sorted(numbers)

print("The sum is: {}".format(running_sum))
print("The Average is {}".format(average))
print("The Largest is {}".format(largest))
print("The Smallest positive number is {}".format(minumum_num_positive))
print("The Sorted numbers are:")
#Iterating through the list number to print out the numbers
#Sorted out seperatedly in a decending order, smallest to hightest.
for num_sort in sort_numbers:
    print(num_sort)


