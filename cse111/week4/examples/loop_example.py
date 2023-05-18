#Loop with a condition

names = ['Jane', 'Mike']
for name in names:
    print(name)
    
print()
print()


for index in range(0, 4):
    print(index)


print()
print()

names = ['fina', 'cash', 'love']
index = 0
names_length = len(names)
while index < names_length:
    print(index)
    #Update index to 1 to stop the loop
    index +=1
    
    
def main():
    total = 0
    
    #get ten or fewer numbers  from the user
    #add  them together
    for i in range(10):
        numbers = float(input("Please enter a number: "))
        if numbers == 0:
            break
        total = total + numbers
    #print the sum of all numbers
    print("Sum: {}".format(total))
        
if __name__ == "__main__":
    main()
