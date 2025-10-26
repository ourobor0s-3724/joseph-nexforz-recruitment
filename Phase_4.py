import re
import os
import json
from prettytable import PrettyTable

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
    contact={'Name':name,'Phone Number':num,'Email Address':email}
    with open('contacts.json','a+') as file:
        file.seek(0)
        try:
            data=json.load(file)
        except:
            data=[]
        data.append(contact)
        file.seek(0)
        file.truncate()
        json.dump(data,file,indent=4)
    print('Contact added...')

def view_contacts():
    table = PrettyTable()
    table.field_names = ["Name", "Phone Number", "Email Address"]
    with open('contacts.json','r') as file:
        data=json.load(file)
    for i in data:
        contact=[i['Name'],i['Phone Number'],i['Email Address']]
        table.add_row(contact)
    print('All contacts')
    print('************')
    print()
    print(table)
    print()

def search_contact():
    try:
        while True:
            search=input('Enter the name to be searched for: ')
            if search.strip()=='':
                print('Invalid input')
            else:
                with open('contacts.json','r') as file:
                    data=json.load(file)
                table = PrettyTable()
                table.field_names = ["Name", "Phone Number", "Email Address"]
                for i in data:
                    if search.lower() in i['Name'].lower():
                        contact=[i['Name'],i['Phone Number'],i['Email Address']]
                        table.add_row(contact)
                if len(table.rows)==0:
                    print('No contacts found')
                else:
                    print(table)
                break
    except:
        print("The file doesn't exist or file is empty")

def delete_contact():
    new_data=[]
    print('WARNING: If more than one contact exists with the same name, all of the said contacts will be deleted')
    try:
        while True:
            delete=input('Enter the name to be deleted: ')
            if delete.strip()=='':
                print('Invalid input')
            else:
                with open('contacts.json','a+') as file:
                    file.seek(0)
                    data=json.load(file)
                    for i in data:
                        if delete.lower()!=i['Name'].lower():
                            new_data.append(i)
                    if data==new_data:
                        print("The name entered doesn't exist")
                        continue
                    else:
                        file.seek(0)
                        file.truncate()
                        json.dump(new_data,file,indent=4)
                        print('Contact deleted')
                break
    except:
        print("The file doesn't exist or file is empty")

while True:
    print()
    print('Contact Book')
    print('************')
    print()
    print('1. Add a new contact')
    print('2. View all contacts')
    print('3. Search for contacts')
    print('4. Delete a contact')
    print('5. Exit')
    print()

    try:
        opt=int(input('Enter option number: '))
    except:
        print('Invalid input')
        Continue()
        continue
    print()
    match opt:
        case 1:
            add_contact()
        case 2:
            view_contacts()
        case 3:
            search_contact()
        case 4:
            delete_contact()
        case 5:
            print('Exiting...')
            break
        case _:
            print('Invalid option')
    Continue()
    print()