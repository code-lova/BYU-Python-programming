#finding the max age and name 

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

final_age = []
final_name = []

for age in people:
    data = age.split()
    
    name = str(data[0])
    age = int(data[1])
    
    final_age.append(age)
    final_name.append(name)
    
max_age = -1
min_age = age
max_person_name = ""
min_person_name = ""


# for i in final_age:
#     if i > max_age:
#         max_age = i

for i, k in enumerate(final_age):
    j = final_name[i] # getting the name of the person here..from final_name list 
    if k > max_age:
        max_age = k
        max_person_name = j
    else:
        if k < min_age:
            min_age = k
            min_person_name = j

print("{} is the oldest in the group with age: {}".format(max_person_name, max_age))
print("{} is the youngest in the group with age: {}".format(min_person_name, min_age))


print()

#lets try another logic to solve thsi problem 
 

new_lists = []

for age in people:
    data = age.split()
    
    new_lists.append(data) #appening the data in one list
    

max_age = -1
min_age = int(data[1])
max_name = ""
min_name = ""

for data in new_lists:
    age = int(data[1])
    name = str(data[0])
    if age > max_age:
        max_age = age
        max_name = name
    else:
        if age < min_age:
            min_age = age
            min_name = name

print("{} is {}yrs old - Oldest".format(max_name, max_age))
print("{} is {}yrs old - Youngest".format(min_name, min_age))
