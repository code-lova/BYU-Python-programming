#Procedural programming
# A Python procedural program for computing the average is shown in example 1.

# Example 1

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total  / len(numbers)
    
    print(f"Average: {average:.2f}")
    
if __name__ == "__main__":
    main()
    
    

#Declarative Programming
#When we use declarative programming to program a computer, 
# we do not focus on the process or steps to accomplish a task, 
# but rather we focus on what we want from the task, or in other words, 
# we focus on the desired result.

#- Example 2

#SELECT AVG(numbers) FROM table;

  # AVG(numbers)
#-----------------
#87.57142857142857


#Functional Programming
#When we use functional programming to program a computer, 
# we focus on the functions necessary to accomplish a task.

# Example 3

from functools import reduce

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")




# Call main to start this program.
if __name__ == "__main__":
    main()
    




#Python Lists Are Objects
#In Python, lists are objects with attributes and methods, 
# and a programmer can modify a list by calling those methods.

# Example 5

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)

    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")

    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"
    print(fabrics)

    # Remove the last element from the fabrics list.
    fabrics.pop()

    # Remove denim from the fabrics list.
    fabrics.remove("denim")
    print(fabrics)


# Call main to start this program.
if __name__ == "__main__":
    main()

