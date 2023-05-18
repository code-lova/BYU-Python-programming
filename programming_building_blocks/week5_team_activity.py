score = int(input("Please enter score to determine grade: "))
last_digit = score % 10
sign = ""

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"
    
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

if score >= 92:
    sign = ""

if letter == "F":
    sign = ""

if letter in ("A","B","C","D"):
    print(f"Congratulations.!! You Passed with a: {letter}{sign}.")
else:
    print(f"SORRY..!! you did poorly, you got an: {letter}{sign}. Try again.")
  
 #This is just an example   
x = 4
y = 10
if x == 5:
    print("a")
    if y == 6:
        print("b")
else:
    print("c")
    
    if y == 10:
        print("d")