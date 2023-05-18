print('Please fill the form to generate an Personal User ID.')
print()
firstname = input('Please enter your firstname: ')
lastname = input('please enter your lastname: ')
job_title = input('Please enter your job title: ')
id_num = input('Enter your ID Number: ')
email_addrs = input('Enter your Email Address: ')
phone = input('Please enter your mobile number: ')

#Ask for additional information from the user
hair_color = input('Enter your hair color: ')
eye_color = input('Enter your eye color: ')
starting_month = input('Your starting month: ')
training = input('Completed Advanced Training Yes/No: ')
print()

print('The ID Card is Generated Below:\n')
print('-------------------------------')
print(f'{lastname.upper()}, {firstname}')
print(f'{job_title.title()}')
print(f'ID: {id_num}')
print(f'{email_addrs.lower()}')
print(f'{phone}')
print()
#Adding additional info with spacing
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {starting_month:14} Training: {training}')

print('-------------------------------')