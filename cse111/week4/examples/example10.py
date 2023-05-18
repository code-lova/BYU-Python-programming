#Values and References

"""
The statement at line 4 stores the value 17 into the variable x.
Line 5 copies the value that is in the variable x into the variable y.
Line 6 prints the values of x and y which are both 17.
Line 7 adds one to the value of x, making its value 18 instead of 17.
Line 8 prints the values of x and y again. The value of x was changed to 18. The value of y remained unchanged
"""


def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Call main to start this program.
if __name__ == "__main__":
    main()