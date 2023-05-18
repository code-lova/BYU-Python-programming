import random

number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
    

for num in range(0, 100):
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))
        


    # for i in range(1, 101):
    #     if i % 3 == 0 and i % 5 == 0:
    #         print("FizzBuzz", end='')
    #     elif i % 3 == 0:
    #         print("Fizz", end='')
    #     elif i % 5 == 0:
    #         print("Buzz", end='')
    #     else:
    #         print(i, end='')

    #     print(" ", end='')
        
        
        
squares = []
for x in range(10):
    squares.append(x**2)
    
print(squares, end=",")

print()

combs = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)
print()

#create a new list with its vale doubled
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

#eliminate negative number in the vec list
for x in vec[:]:
    if x >= 0:
        print(x, end=",")

print()
for x in vec[:]:
    print(abs(x), end=" ")
    
print()

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
#best method
print([weapon.strip() for weapon in freshfruit])

#another method
fresh = []
for weapon in freshfruit[:]:
    weapon = weapon.strip()
    fresh.append(weapon)
print(fresh)
    
print()
# create a list of 2-tuples like (number, square)
for x in range(6):
    print("{}".format([(x, x**2)]), end=",")

print()
    
#SETS 
 # show that duplicates have been removed
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}   
print(basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a) # unique letters in a
print(a | b) # letters in a or b or both
print(a - b) # letters in a but not in b
print(a & b) # letters in both a and b
print(a ^ b)  # letters in a or b but not both

print()
#Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 8829
print(tel)
print(tel['jack'])

del tel['sape']
tel['irvi'] = 7830
print(tel)

print()

#looping techniques
#When looping through dictionaries, the key and corresponding
# value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print()

#To loop over two or more sequences at the same time, 
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


print()

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
basket = sorted(basket)
for i in basket:
    print(i)

    
print()

#Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a
# sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
basket.sort()
for fruit in set(basket):
    print(fruit)
    
print()

#It is sometimes tempting to change a list while you are looping over it; however, 
# it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)