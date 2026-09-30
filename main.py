import check_input
from contact import Contact

def read_file():
    contacts = []
    with open('addresses.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                fn, ln, ph, addr, city, zip = line.split(',')
                contacts.append(Contact(fn, ln, ph, addr, city, zip))
    contacts.sort()
    return contacts

def write_file(contacts):
    None

def get_menu_choice():
    None

def modify_contact(cont):
    None

def main():
    read_file()
