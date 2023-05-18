people  = ["james","Hanna","Rita","Matter","John","Jessica","Aboy"]
person = people[3:-3]
print(person)

a = "school is cool"
pick = a[1:-5]
print(pick)

word = "Holberton"
word_first_3 = word[0:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]

print(word_first_3)
print(word_last_2)
print(middle_word)

#Converting this string to print = object oriented programming with python
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

str = str[39:66] + "" + str[106:111] + " " + str[:6]

print(str)


