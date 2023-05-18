#Purpose: A program to determine whether to loan
#loan money based on the data collected from user
print("On a scale of 1-10, please answer these questions.")
loan_size = int(input("How large is the loan: "))
credit_history = int(input("How good is your credit history: "))
income_amount = int(input("How high is your income: "))
down_payment = int(input("How large is your down payment: "))

should_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income_amount >= 7:
        should_loan = True
    elif credit_history >=7 or income_amount >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False

else:
    if credit_history < 4:
        should_loan = False
    else:
        if income_amount >= 7 or down_payment >= 7:
            should_loan = True
        elif income_amount >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False
    
if should_loan == True:
    print("The decision is yes. This is a good loan")
else:
    print("The decision is no. You should not loan this money.")

