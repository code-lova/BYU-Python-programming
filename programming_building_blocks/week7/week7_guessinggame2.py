import random

#Load words and store them in a list
word_list = []
word_file = open("words.txt")
for word in word_file:
    word_list.append(word.strip())
    
#pick a word from the list
#storing the answer in the variable called answer
answer = random.choice(word_list)
print(answer) #But lets pretend  we dont know the answer 
num_of_guesses = 0
guess = "unknown"
answer_length = 5


while guess not in answer:
    guess = str(input("What is yor guess: "))
    if guess == "":
        print("Invalid Response")
        guess = str(input("What is yor guess: "))
        guess = guess.lower()
        if guess not in answer:
            print("Your guess was not correct.")
            print("You guessed: {}".format(guess))
            num_of_guesses += 1
        else:
            print("Congratulations..!! you guessed the right word")
            print("It took you {} guesses".format(num_of_guesses))
    else:
        guess = guess.lower()
        if guess not in answer:
            print("Your guess was not correct.")
            print("You guessed: {}".format(guess))
            num_of_guesses += 1
        else:
            print("Congratulations..!! you guessed the right word")
            print("It took you {} guesses".format(num_of_guesses))
        
    


    
    
            
    

    

    
    