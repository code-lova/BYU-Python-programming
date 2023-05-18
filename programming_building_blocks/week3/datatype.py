days_of_feb = 28
#more preferrable way to add or treat numbers as strings 
print(str(days_of_feb) + ' days in febuary')

#Another alternate way to do that.
print(f'{days_of_feb} days in febuary')

#getting user input
first_num = input('Enter first number: ')
sec_num = input('Enter second num: ')

print(float(first_num) + float(sec_num))

#maths operation 
# one = 6
# two = 8
# print(one ** two)

# color = 'blue'
# color2 = 'red'
#Both of this two will yield same result
# print(f'{color} {color2}') 
# print(color + ' ' + color2)

# combine_words = color + ' ' + color2 + '!'
# print(combine_words)

number1 = str(4)
print('The number is '+ number1 +' total')

number1 = 11
print('The number is '+ str(number1) +' total')

number_people = input('How many people are in the church: ')
result = int(number_people)
count_double = result * 2
print(count_double)