def main_menu():
    contacts = load_contacts()  # Load contacts from file on startup
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")
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
            search_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")