import re

while True: 
    name=input('Enter name: ')
    if re.search(r"^[a-zA-Z.` -]+$",name):
        break
    else:
        print('Please enter a name...')
while True:
    num=input('Enter phone number: ')
    if len(num)==10 and num.isdigit():
        break
    else:
        print('Please enter a valid phone number...')
while True:
    email=input('Enter email address: ')
    if re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
        break
    else:
        print('Please enter a valid email address...')

print(f'\nName: {name.title()}\nPhone number: {num}\nEmail address: {email}')
