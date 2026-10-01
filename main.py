import check_input
from contact import Contact

def read_file():
    contacts = []
    with open('addresses.txt') as file:
        for line in file:
            line = line.strip()
            if line is None:
                fn, ln, ph, addr, city, zip = line.split(',')
                contacts.append(Contact(fn, ln, ph, addr, city, zip))
    contacts.sort()
    return contacts

def write_file(contacts):
    with open('addresses.txt', 'w') as file:
        for cont in contacts:
            file.write(repr(cont) + '\n')

def get_menu_choice():
    return check_input.get_int_range('Rolodex Menu:\n1. Display Contacts\n2. Add Contacts\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit', 1, 5)

def modify_contact(cont):
    choice = 0
    while choice != 7:
        choice = check_input.get_int_range('Modify Menu:\n1. First Name\n2. Last Name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save', 1, 7)
        if choice == 1:
            cont.fn = input('Enter first name: ')
        elif choice == 2:
            cont.ln = input('Enter last name: ')
        elif choice == 3:
            cont.ph = input('Enter phone #: ')
        elif choice == 4:
            cont.addr = input('Enter Address: ')
        elif choice == 5:
            cont.city = input('Enter city: ')
        elif choice == 6:
            cont.zip = input('Enter zip: ')

def display_contacts(contacts):
    print(f'Number of contacts: {len(contacts)}')
    for i in range(len(contacts)):
        print(f'{i + 1}. {contacts[i]}')

def add_contact(contacts):
    print('Enter new contact:')
    fn = input('First name: ')
    ln = input('Last name: ')
    ph = input('Phone #: ')
    addr = input('Address: ')
    zip = input('Zip: ')
    contacts.append(Contact(fn, ln, ph, addr, zip))
    contacts.sort()

def main():
    read_file()
