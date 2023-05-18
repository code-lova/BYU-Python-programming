# This week we talked about lists in python

name = []
names = ["james","victory","victor","John"]
print(names)
#Or we could say iterate through the list and print each string one after the other
#seperately
for client in names:
    print(client)
    
# we can also ask for more to add them on the list 

new_client = ""
end_prog = "quit"
while new_client !=end_prog: 
    new_client = input("what is the name of the client?: ")
    #Here we are appending what every name as input was given
    #And adding it to name, which was decleared up as an empty LIST
    name.append(new_client)
    #Then we iterate through it to print what name has hold from the input
    #As namez, 
for namez in name:
    print(namez) 
    
