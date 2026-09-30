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
        for contact in contacts:
            file.write(repr(contact) + '\n')

def get_menu_choice():
    return check_input.get_int_range('Rolodex Menu:\n1. Display Contacts\n2. Add Contacts\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit', 1, 5)

def modify_contact(cont):
    None

def main():
    read_file()
