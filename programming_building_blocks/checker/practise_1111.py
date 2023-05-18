people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

final = []

for persons in people:
    peop = persons.split(' ')
    # print(peop)
    final.append(peop)


youngest_age = float(peop[1])
youngest_name = ''

for item in final:

    name = item[0]
    age = float(item[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f'the youngest person is {youngest_name} and he is {youngest_age} years old.')



    
     



