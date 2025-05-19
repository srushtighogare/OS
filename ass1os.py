import os
import json

# File to store the address book
FILENAME = "address_book.json"

# Load address book from file
def load_address_book():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return {}

# Save address book to file
def save_address_book(book):
    with open(FILENAME, 'w') as f:
        json.dump(book, f, indent=4)

# Create a new address book
def create_address_book():
    return {}

# View the address book
def view_address_book(book):
    if not book:
        print("\nAddress Book is empty.\n")
        return
    print("\nAddress Book:")
    for name, info in book.items():
        print(f"\nName: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print(f"  Address: {info['address']}")
    print()

# Insert a new record
def insert_record(book):
    name = input("Enter name: ")
    if name in book:
        print("Record already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    book[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Record added successfully.")

# Delete a record
def delete_record(book):
    name = input("Enter name to delete: ")
    if name in book:
        del book[name]
        print("Record deleted successfully.")
    else:
        print("Record not found.")

# Modify a record
def modify_record(book):
    name = input("Enter name to modify: ")
    if name in book:
        print("Leave blank to keep current value.")
        phone = input(f"Enter new phone [{book[name]['phone']}]: ") or book[name]['phone']
        email = input(f"Enter new email [{book[name]['email']}]: ") or book[name]['email']
        address = input(f"Enter new address [{book[name]['address']}]: ") or book[name]['address']
        book[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Record updated successfully.")
    else:
        print("Record not found.")

# Main program
def main():
    address_book = load_address_book()

    while True:
        print("\n--- Address Book Menu ---")
        print("a) Create Address Book")
        print("b) View Address Book")
        print("c) Insert Record")
        print("d) Delete a Record")
        print("e) Modify a Record")
        print("f) Exit")
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            address_book = create_address_book()
            print("New address book created.")
        elif choice == 'b':
            view_address_book(address_book)
        elif choice == 'c':
            insert_record(address_book)
        elif choice == 'd':
            delete_record(address_book)
        elif choice == 'e':
            modify_record(address_book)
        elif choice == 'f':
            save_address_book(address_book)
            print("Address book saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
