#Values and referencing 

"""

    The statement at line 4 creates a list and stores a reference to that list in the variable lx.
    Line 5 copies the reference in the variable lx into the variable ly. Line 5 does not create a copy of the list 
    but instead causes both the variables lx and ly to refer to the same list.
    Line 6 prints the values of lx and ly. Notice that their values are the same as we expect them to be because of line 5.
    Line 7 appends the number 5 onto the list lx.
    Line 8 prints the values of lx and ly again. Notice in the output that when lx and ly are printed the second time, 
    it appears that the number 5 was appended to both lists.

"""

# Example 11

def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

# Call main to start this program.
if __name__ == "__main__":
    main()