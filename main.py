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
    with open('addresses.txt', 'w') as file:
        for cont in contacts:
            file.write(repr(cont) + '\n')

def get_menu_choice():
    return check_input.get_int_range('Rolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit\n', 1, 5)

def modify_contact(cont):
    choice = 0
    while choice != 7:
        choice = check_input.get_int_range('Modify Menu:\n1. First name\n2. Lastname\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save\n', 1, 7)
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
    city = input('City: ')
    zip = input('Zip: ')
    contacts.append(Contact(fn, ln, ph, addr, city, zip))
    contacts.sort()

def search_contacts(contacts):
    choice = check_input.get_int_range('Search:\n1. Search by last name\n2. Search by zip', 1, 2)
    if choice == 1:
        info = input('Enter last name: ')
    else:
        info = input('Enter zip code: ')

    found = False
    for cont in contacts:
        if choice == 1 and cont.ln.lower() == info.lower():
            print(cont)
            found = True
        elif choice == 2 and cont.zip == info:
            print(cont)
            found = True
    if not found:
        print('No matches found.')

def find_contact(contacts, fn, ln):
    for cont in contacts:
        if cont.fn.lower() == fn.lower() and cont.ln.lower() == ln.lower():
            return cont
    return None

def main():
    contacts = read_file()
    choice = 0
    while choice != 5:
        choice = get_menu_choice()
        if choice == 1:
            display_contacts(contacts)
        elif choice == 2:
            add_contact(contacts)
        elif choice == 3:
            search_contacts(contacts)
        elif choice == 4:
            fn = input('Enter first name: ')
            ln = input('Enter last name: ')
            cont = find_contact(contacts, fn, ln)
            if cont is None:
                print('Contact not found.')
            else:
                print(cont)
                modify_contact(cont)
                contacts.sort()
        elif choice == 5:
            print('Saving File...')
            write_file(contacts)
            print('Ending Program')

if __name__ == '__main__':
    main()
