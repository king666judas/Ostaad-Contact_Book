# main_menu.py
# Main entry point of the program.

from contact_operations import add_contact, edit_contact, search_contacts, remove_contact
from file_handler import save_contacts, load_contacts
from utilities import view_contacts

'''
>> Main Menu:
    > Displays the menu options to the user.
    > Routes user choices to the corresponding functions (e.g., Add Contact, Edit Contact).
    > Returns to the menu after completing operations or exits the program.
'''
def main_menu():
    contacts = load_contacts()  # Load contacts from file on startup
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Edit Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)  # Save after addition
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            remove_contact(contacts)
            save_contacts(contacts)  # Save after removal
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            edit_contact(contacts)
            save_contacts(contacts)  # Edit after addition
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()