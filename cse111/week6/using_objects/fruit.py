#Write a small Python program named fruit.py that 
# demonstrates object oriented programming by modifying a list. 

def main():
    #create and print a list of named fruit.
    fruits_list = ["pear", "banana", "apple", "mango"]
    print()
    print("Original Fruit list")
    for k, fruits in enumerate(fruits_list):
        print("{}. {}".format(k, fruits))
    
    print()   
    print("Reverse fruit list:")
    fruits_list.reverse()
    for each_fruit in fruits_list:
        print(each_fruit)
        
    print()
    print("Add orange to the end of the list:")
    fruits_list.append("orange")
    for each_fruit in fruits_list:
        print(each_fruit)
        
    print()
    print("Insert cherry to the fruit list before apple:")
    fruits_list.insert(1, "cherry")
    for each_fruit in fruits_list:
        print(each_fruit)  
     
    print()
    print("Remove Banana from the fruit list:")
    banana_index = fruits_list[3]
    fruits_list.remove(banana_index)
    for each_fruit in fruits_list:
        print(each_fruit)  
    
    print()
    print("Pop the last element from the list:")
    fruits_list.pop()
    for each_fruit in fruits_list:
        print(each_fruit) 
        
    print()
    print("Sort the fruit list:")
    fruits_list.sort()
    for each_fruit in fruits_list:
        print(each_fruit) 
        
    print()
    print("Clear the fruit list:")
    fruits_list.clear()
    print(fruits_list) 
        
    pass



if __name__ == "__main__":
    main()