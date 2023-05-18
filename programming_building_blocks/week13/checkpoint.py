#Calling functions from modules files
from modules import display_regular, display_uppercase, display_lowercase

#Receives user input and displays it as it is.
#Receives user input and displays it as UPPERCASE
#Receives user input and displays it as lowercase


print("What is your message: ",end=" ")
user_message = str(input(""))
user_message = display_regular(user_message) #calling the display_regular function here after importing it
user_message2 = display_uppercase(user_message) #calling the display_uppercase function here after importing it
user_message3 = display_lowercase(user_message) #calling the display_lowercase function here after importing it

print(user_message)
print(user_message2)
print(user_message3)



