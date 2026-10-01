# Julian Cervantes
# Abdallah Salameh
# Group 4
# OpOverload - a program that manages a contact list

# Imports
import check_input
from contact import Contact

def read_file():
    '''Reads the contacts from the file and returns a list of Contact objects
    
    Returns:
        list: a list of Contact objects
    '''

    # Initialize an empty list
    contacts = []
    # Read the file and create a Contact object for each line
    with open('addresses.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                fn, ln, ph, addr, city, zip = line.split(',')
                # Create a Contact object and add it to the list
                contacts.append(Contact(fn, ln, ph, addr, city, zip))
    # Sort the contacts by last name then by first name
    contacts.sort()
    return contacts

def write_file(contacts):
    '''Writes the contacts to the file
    
    Args:
        contacts (list): a list of Contact objects
    '''

    # Write the contacts to the file in the format fn, ln, ph, addr, city, zip
    with open('addresses.txt', 'w') as file:
        for cont in contacts:
            file.write(repr(cont) + '\n')

def get_menu_choice():
    '''Displays the menu and gets the user's choice
    
    Returns:
        int: the user's choice
    '''

    # Displays the menu and gets the user's choice
    return check_input.get_int_range('Rolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit\n', 1, 5)

def modify_contact(cont):
    '''Modifies the contact's information
    
    Args:
        cont (Contact): the contact to modify
    '''

    # Initialize the choice to 0
    choice = 0

    # Loop until the user chooses to save and quit
    while choice != 7:
        choice = check_input.get_int_range('Modify Menu:\n1. First name\n2. Last name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save\n', 1, 7)
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
    '''Displays the contacts in the list
    
    Args:
        contacts (list): a list of Contact objects
    '''

    # Displays the number of contacts and each contact in the list
    print(f'Number of contacts: {len(contacts)}')
    for i in range(len(contacts)):
        print(f'{i + 1}. {str(contacts[i])}')

def add_contact(contacts):
    '''Adds a new contact to the list
    
    Args:
        contacts (list): a list of Contact objects
    '''

    # Prompts the user for the contact's information and adds it to the list
    print('Enter new contact:')
    fn = input('First name: ')
    ln = input('Last name: ')
    ph = input('Phone #: ')
    addr = input('Address: ')
    city = input('City: ')
    zip = input('Zip: ')

    # Creates a new Contact object and adds it to the list
    contacts.append(Contact(fn, ln, ph, addr, city, zip))

    # Sorts the contacts by last name then by first name
    contacts.sort()

def search_contacts(contacts):
    '''Searches for contacts by last name or zip code
    
    Args:
        contacts (list): a list of Contact objects
    '''

    # Prompts the user for the search criteria
    choice = check_input.get_int_range('Search:\n1. Search by last name\n2. Search by zip\n', 1, 2)

    # Prompts the user for the search information
    if choice == 1:
        info = input('Enter last name: ')
    else:
        info = input('Enter zip code: ')

    # Searches for the contacts and displays the results
    found = False
    for cont in contacts:
        if choice == 1 and cont.ln.lower() == info.lower():
            print(str(cont))
            found = True
        elif choice == 2 and cont.zip == info:
            print(str(cont))
            found = True
    if not found:
        print('No matches found.')

def find_contact(contacts, fn, ln):
    '''Finds a contact by first and last name
    
    Args:
        contacts (list): a list of Contact objects
        fn (str): first name
        ln (str): last name

    Returns:
        Contact: the contact if found and None if not found
    '''

    # Searches for the contact in the list and returns it if found
    for cont in contacts:
        if cont.fn.lower() == fn.lower() and cont.ln.lower() == ln.lower():
            return cont
    return None

def main():
    '''Main function that runs the program'''

    # Reads the contacts
    contacts = read_file()

    # Displays the menu and gets the user's choice until they choose to save and quit
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
                print(str(cont))
                modify_contact(cont)
                contacts.sort()
        elif choice == 5:
            print('Saving File...')
            write_file(contacts)
            print('Ending Program')

# Runs the main function
if __name__ == '__main__':
    main()
