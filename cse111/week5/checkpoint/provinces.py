#Write a Python program named provinces.py that reads the contents of 
# provinces.txt into a list and then modifies the list.

def main():
    
    entire_list = read_content("provinces.txt")
    
    print(entire_list)
    
    # Remove the first element from the list.
    entire_list.pop(0)
    #print(entire_list)

    # Remove the last element from the list.
    entire_list.pop()
    #print(entire_list)
    
   # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(entire_list)):
        if entire_list[i] == "AB":
            entire_list[i] = "Alberta"
    #print(entire_list)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = entire_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")

    
    pass



def read_content(filename):
    
    new_list = []
    
    with open(filename, mode="rt") as province_list:
        
        for province in province_list:
            
            province = province.strip()
            
            new_list.append(province)
            
    return new_list



if __name__ == "__main__":
    main()            
