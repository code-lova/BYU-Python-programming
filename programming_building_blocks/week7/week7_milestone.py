import random
#Load words and store them in a list
word_list = []
# word_file = open("words.txt")
# for word in word_file:
#     word_list.append(word.strip()) 
    
with open("words.txt") as word_file:
    for words in word_file:
        words = words.strip()
        word_list.append(words)
        
    
#pick a word from the list
#storing the answer in the variable called answer

answer = random.choice(word_list)
#print(answer) Lets choose not to display the anser yet
guess = "unknown"
num_of_guesses = 0
hint = ""
position = 0

print("---WORDLE GUESSING GAME---\nThere is a secrete word, you must guess what it is...")
print("You only have 5 guesses")

#INITIAL HINT
print("\nYour hint is: " + " _ " * len(answer))

guess = str(input("What's your guess?: "))
guess = guess.lower()
num_of_guesses += 1

if guess == "": #Checking if the user's response is valid. If the user does not enters any word, end the game
    print("SORRY NOT ALLOWED. GAME OVER.!!!")
else:
    while guess not in answer and num_of_guesses <= 5:
        print("Your guess was not correct.")
        for user_guesses in guess: #LOOP THE GUESS
        #CATCH ERROR IF 5+ LETTERS
            try:
                if user_guesses == answer[position]:#CAPS LETTERS
                    hint +=  " " + user_guesses.upper() + " "
                elif user_guesses in answer: #LOWER LETTERS
                    hint +=  " " + user_guesses.lower() + " "
                else: #UNDERLINES
                    hint += " _ " 
            except:
                print("More than 5 letter words aren't allowed. Try again!")
                hint = " _ " * len(answer) #store the initial hint in the hint variable
                break
        
            position += 1
    
        print("Your hint is: {}".format(hint))        
        guess = input("What's your guess?: ")
        
        #RESET VARIABLES
        hint = ""
        position = 0
        num_of_guesses += 1
        
    #FINAL
    if num_of_guesses > 5:
        print("Sorry.!! You ran out of guesses.")
        print("You didn't guess the word! GAME OVER.")
        print("The SECRETE word was: {}.".format(answer.upper())) #Displaying the secrete word after the program
        
    else:
        if guess == "":
            print("Invalid Response. GAME OVER.!!!")
        else:
            if guess in answer:
                print("\nCongratulations! You guessed the word.")
                print(f"It took you {num_of_guesses} guesses.")
                print("The SECRETE word was: {}.".format(answer.upper())) #Displaying the secrete word after the program 
                print("--------------------------------------")

    


            
            
    
        
    