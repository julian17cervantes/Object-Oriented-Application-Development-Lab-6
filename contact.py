class Contact:
    '''A Contact in a rolodex

    Attributes:
        fn (str): first name
        ln (str): last name
        ph (str): phone number
        addr (str): address
        city (str): city
        zip (str): zip code
    '''

    def __init__(self, fn, ln, ph, addr, city, zip):
        '''Initializes a Contact with the given information

        Args:
            fn (str): first name
            ln (str): last name
            ph (str): phone number
            addr (str): address
            city (str): city
            zip (str): zip code
        '''

        # Assigns each parameter to its attribute
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        '''Compares 2 contacts by last name, then by first name
        Args:
            other (Contact): the other Contact to compare to

        Returns:
            bool: True if this Contact comes before other Contact in sort order
        '''

        # Compares last name first, then compares by first name if last names are the same
        if self.ln == other.ln:
            return self.fn < other.fn
        return self.ln < other.ln


    def __str__(self):
        ''' Creates a string for displaying the contact information
        
        Returns:
            str: the string representation of the contact
        '''

        # Return a string with each piece of information on its own separate line
        return (f'{self.fn} {self.ln}\n{self.ph}\n{self.addr}\n{self.city} {self.zip}')

    def __repr__(self):
        '''Creates a string for writing the contact to the file
        
        Returns:
            str: the contact in the format fn, ln, ph, addr, city, zip
        '''

        # Return a string with each piece of information seperated by a comma
        return (f'{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}')