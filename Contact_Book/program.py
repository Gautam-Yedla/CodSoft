import re

# Function to validate phone number (10 digits only)
def is_valid_phone(phone):
    return re.fullmatch(r'\d{10}', phone) is not None

# Function to validate email address
def is_valid_email(email):
    # Simple regex pattern to validate email addresses
    return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email) is not None

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()
    
    while True:
        phone = input("Enter 10-digit phone number: ").strip()
        if is_valid_phone(phone):
            break
        else:
            print("Invalid phone number! Please enter a 10-digit phone number.")
    
    while True:
        email = input("Enter email address: ").strip()
        if is_valid_email(email):
            break
        else:
            print("Invalid email address! Please enter a valid email (e.g., example@domain.com).")
    
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter the name or phone number to search: ").strip()
    
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term == info['phone']:
            print(f"\nContact Found: \nName: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            return
    print("Contact not found.")

# Function to update a contact's details
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    
    if name in contacts:
        print("What would you like to update?")
        print("1. Phone Number")
        print("2. Email")
        print("3. Address")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            while True:
                new_phone = input("Enter the new 10-digit phone number: ").strip()
                if is_valid_phone(new_phone):
                    contacts[name]['phone'] = new_phone
                    break
                else:
                    print("Invalid phone number! Please enter a 10-digit phone number.")
        
        elif choice == '2':
            while True:
                new_email = input("Enter the new email: ").strip()
                if is_valid_email(new_email):
                    contacts[name]['email'] = new_email
                    break
                else:
                    print("Invalid email address! Please enter a valid email (e.g., example@domain.com).")
        
        elif choice == '3':
            new_address = input("Enter the new address: ").strip()
            contacts[name]['address'] = new_address
        else:
            print("Invalid choice.")
        
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

# Main function to interact with the user
def contact_book():
    while True:
        print("\n<<<<<<<<<<............Contact Book Menu..............>>>>>>>>>>>")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book
if __name__ == "__main__":
    contacts = {}
    contact_book()




