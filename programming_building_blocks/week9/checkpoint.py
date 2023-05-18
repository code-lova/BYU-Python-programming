#A program that request for user input as friends name
#And adding them to a list then when they are done
#They type end and they see list of names inputed to the list.

print("--Enter a new frineds name and when done type 'end' to end program.--- ")
names = []

end_prog = "end"
new_friend = ""

while new_friend != end_prog:
    new_friend = str(input("Type the name of your friend: "))
    if new_friend != "end":
        names.append(new_friend)
print("Your friends name are:")
for new_name in names:
    print(new_name)
    
