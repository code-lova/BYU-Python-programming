#A program to ask the ser for a bank account and its accont balance

bank_account_name = []
account_balance = []

acc_name = ""
end_prog = "quit"

running_total = 0

answer = ""
stop = "no"

name = None

print()
print("Enter the name and balance of the accounts (Type: quit to when done)")
print()

while acc_name != end_prog:
    print("What is the name of the account?:", end=" ")
    acc_name = str(input(""))
    acc_name = acc_name.lower()
    if acc_name != "quit":
        print("What is the balance?: ",end=" ")
        acc_bal = float(input(""))
        if acc_name != "quit":
            bank_account_name.append(acc_name)
            account_balance.append(acc_bal)
    else:
        print()

print("Account Information:")
for i, acc_names in enumerate(bank_account_name):
    acc_bals = account_balance[i]
    print("{}. {} - ${:,.2f}\n".format(i, acc_names, acc_bals))

#find the sum of all account balance
for amount in account_balance:
    running_total += amount
    
#finding the average
length = len(account_balance)
average = running_total / length

#finding highest balance
highest_name = None
highest_balance = -1

for m, number in enumerate(bank_account_name):
    namezz = bank_account_name[m]
    acc_balz = account_balance[m]
    
    if acc_balz > highest_balance:
        highest_balance = acc_balz #highest balance
        highest_name = namezz #highest name

print()
print("Total: ${:,.2f}".format(running_total))
print("Average: ${:,.2f}".format(average))
print("Highest Balance: {} - ${:,.2f}".format(highest_name, highest_balance))

print()

while answer != stop:
    print("Do you want to udate an account(yes/no)?: ",end=" ")
    answer = str(input(""))
    answer = answer.lower()
    if answer == "yes":
        print("What account index do you want to update?:",end=" ")
        acc_index_to_update = int(input(""))
        print("What is the new amount: ",end=" ")
        acc_amount_to_update = float(input(""))
        
        account_balance[acc_index_to_update] = acc_amount_to_update
        print()
        print("Account Information:")
        for j, acc_names in enumerate(bank_account_name):
            acc_bals = account_balance[j]
            print("{}. {} - ${:,.2f}".format(j, acc_names, acc_bals))
            print()
    else:
       print()

print("Account Information:")
for k, acc_names in enumerate(bank_account_name):
    acc_bals = account_balance[k]
    print("{}. {} - ${:,.2f}\n".format(k, acc_names, acc_bals))  
    