from array import array

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

names = ['james', 'jake']
print(len(names))
names.insert(0, 'bill')
print(names)
names.sort()
print(names)

print()
print()

names = ['jessica', 'franka', 'Mila', 'John']
presenter = names[1:3]
print(names)
print(presenter)

print()
print()
#Dictionaries
#They have key values that helps us
#identity object in an array

person = {'first': 'Christ'}
person['last'] = 'Harrison'
print(person)
print(person['first'])