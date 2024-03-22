from collections import defaultdict

class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name:str, phone:str, email:str=None):
        """
        Add a new contact

        :param name: Contact name to be added
        :param phone: Contact phone
        "param email: Contact email
        """
        if name in self.contacts:
            print("contact already existed")
            return
        
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email

    def view_contacts(self):
        """
        view all of the contacts in the book
        """

        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"phone: {info['phone']}")
            print(f"email: {info['email']}")
            print("-"*20)

    def update_contact(self, name:str, new_name:str=None, phone:str=None, email:str=None):
        """
        Update the contact information

        :param name: Contact name to be added
        :param new_name: Contact updated name
        :param phone: Contact updated phone
        "param email: Contact updated email
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if new_name:
                self.contacts[new_name] = self.contacts[name]
                del self.contacts[name]
        else:
            print("Contact not found!")

        print("Contact Updated Successfully")
        return


    def delete_contact(self, name:str):
        """
        Delete contact from the book

        :param name: contact name to be deleted
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact Deleted Successfully")
        else:
            print("Contact not found!")

if __name__ == "__main__":
    book = ContactBook()

    while True:
        print('\n\nContact Book Application')
        print('1. Add_Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Quit')

        user_choice = input("Please choose an option: ")

        if user_choice == '5':
            break
        elif user_choice == '1':
            name = input('\nEnter Contact Name: ')
            phone = input('Enter Contact Phone: ')
            email = input('Enter Contact email: ')

            book.add_contact(name, phone, email)
        elif user_choice == '2':
            print("\n\n\nList of Contacts:")
            book.view_contacts()

        elif user_choice == '3':
            name = input('\nEnter Contact Name: ')
            new_name = input('\nEnter Contact New Name: ')
            phone = input('Enter Contact Phone: ')
            email = input('Enter Contact email: ')

            book.update_contact(name, new_name, phone, email)
        elif user_choice == '4':
            name = input('\nEnter Contact Name: ')

            book.delete_contact(name)
