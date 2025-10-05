import re
import os

contacts=[]
def Continue():
    input('Press enter to continue...')
    os.system('cls')

def add_contact():
    while True: 
        name=input('Enter name: ')
        if re.search(r"^[a-zA-Z.` -]+$",name):
            break
        else:
            print('Please enter a valid name...')
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
    contacts.append([name,num,email])
    print('Contact added...')
    Continue()

def view_contacts():
    print('All contacts')
    print('************')
    print()
    print('Name | Phone Number | Email Address')
    print('-----------------------------------')
    for i in contacts:
        print(f'{i[0]} | {i[1]} | {i[2]}')
    print()
    Continue()

while True:
    print()
    print('Contact Book')
    print('************')
    print()
    print('1. Add a new contact')
    print('2. View all contacts')
    print('3. Exit')
    print()
    opt=int(input('Enter option number: '))
    print()
    match opt:
        case 1:
            add_contact()
        case 2:
            view_contacts()
        case 3:
            print('Exiting...')
            break
        case _:
            print('Invalid option')
            Continue()
    print()
