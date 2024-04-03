# Contact Book Application

This Python script implements a simple contact book application.

## Features

- **Add Contact**: Add a new contact with a name, phone number, and email address. Prevents adding duplicate contacts.

- **View Contacts**: Display all stored contacts, including their name, phone number, and email address.

- **Update Contact**: Modify existing contact information, including the name, phone number, or email address.

- **Delete Contact**: Remove a contact from the contact book.

- **Quit**: Exit the application.

## Class Structure

The script includes a `ContactBook` class with the following methods:

- `add_contact(name, phone, email)`: Add a new contact.
- `view_contacts()`: Display all contacts.
- `update_contact(name, new_name, phone, email)`: Update existing contact information.
- `delete_contact(name)`: Delete a contact.
- `__init__()`: Initialize the contact book.

## Usage

1. Run the script.
2. Choose an option from the menu:
   - Add a contact
   - View contacts
   - Update contact
   - Delete contact
   - Quit

Follow the prompts to perform the desired action.