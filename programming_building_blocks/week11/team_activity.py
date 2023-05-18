#Still working with opening and reading from file
#Assignment

with open("hr_system.txt") as records:
    for employee in records:
        employee = employee.strip()
        each_details = employee.split()
        
        employee_name = each_details[0]
        employee_title = each_details[2]
        
        print("Name: {}, Title: {}".format(employee_name, employee_title))
        
print()
print("--Stretch assignemnt below--")
#Stretch assignment below

payment_amount = 0

with open("hr_system.txt") as records:
    for employee in records:
        employee = employee.strip()
        each_details = employee.split()
        
        employee_name = each_details[0]
        employee_title = each_details[2]
        employee_Id = int(each_details[1])
        employee_salary = float(each_details[3])
        
        #paychecks calculations assuming they are payed twice a month
        payment_amount = employee_salary / 24
        
        #Adding bonus to employees who are engineers
        if employee_title.title() == "Engineer":
            payment_amount += 1000
        
        print("{} (ID: {}), {} - ${:,.2f}".format(employee_name, employee_Id, employee_title, payment_amount))