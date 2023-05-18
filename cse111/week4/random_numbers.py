#Create a list of numbers
import random



def main():
    numbers = [16.2, 75.1, 52.3]
    numbers_list = numbers
    print(numbers)
   
   #This function was given one arguement to add a single number 
   #to numbers list
    append_random_numbers(numbers_list)
    print(numbers)
    
    #here same function was given 2 arguement to add quantity amount of
    #numbers to the numbers list
    append_random_numbers(numbers_list, quantity=3)
    print(numbers)
    
    
    
    #  ---THIS IS A SEPERATE PROGRAM ---
    #Callin the append_random_words function to 
    #append and print the words to the old_words list
    old_words = ["meet", "fun", "dear"]
    words_list = old_words

    append_random_words(words_list, quantity=4)
    print(old_words)
    
    
    pass




def append_random_numbers(numbers_list, quantity=1):
    """Python program named random_numbers.py that creates a list of numbers, appends 
    more numbers onto the list, and prints the list. 
    The program must have two functions named
    main and append_random_numbers

    Args:
        numbers_list (foat): An empty list that will hold floating numbers
        quantity (int, optional): This is set as a condition.
        given a default value. Defaults value to 1.

    Returns:
        Float: list
    """
    if quantity == 1:
        numbers = random.uniform(15, 8)
        round_numbers = round(numbers, 1)
        numbers_list.append(round_numbers)
    else:
        for i in range(quantity):
            numbers = random.uniform(25, 10)
            round_numbers = round(numbers, 1)
            
            numbers_list.append(round_numbers)
        
        return numbers
    
    
    
def append_random_words(words_list, quantity=1):
    """Python program named append_random_words.py that creates a list of words, appends 
    more strings onto the list, and prints the list. 
    The program must have two functions named
    main and append_append_random_words

    Args:
        words_list (string): list
        quantity (int, optional): quantity of string to be added to the list. Defaults to 1.

    Returns:
        srting: words list
    """
    if quantity == 1:
        words = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
                "join", "laugh", "love", "sleep", "smile", "speak",
                "sunshine", "toothbrush", "tree", "truth", "walk", "water"]
        words = random.choice(words)
        words_list.append(words)
    else:
        for j in range(quantity):
            words = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
                    "join", "laugh", "love", "sleep", "smile", "speak",
                    "sunshine", "toothbrush", "tree", "truth", "walk", "water"]
            words = random.choice(words)
            words_list.append(words)
            
        return words
        

if __name__ == "__main__":
    main()