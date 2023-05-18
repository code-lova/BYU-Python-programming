#Defining all my dodules here to be sed in scriptd.py

def namer(name):
    print("Hello there " + name)

def add(a,b):
    return (a + b)

#what this function does is that it sort the given numbers from the python code
#Then substract the lowest from the highest
def stat_range(data):
    data.sort()
    return data[-1] - data[0]

#This function prints the initials of the users name
#setting default force_ppercase to TRUE in the paramenter or not if u choose to
#But if you dont set its default dont forget to set when calling the fuction in the other file
def get_initials(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

