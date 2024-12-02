from utilities import save_contacts
from validate_input import validate_input

def remove_contact(contacts):
    while True:
        print("\n--- Remove Contact ---")
        print("1. Remove a Contact")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "2":
            print("Returning to main menu...")
            break

        if choice == "1":
            phone = input("Enter the phone number of the contact to remove: ").strip()

            is_valid, error_message = validate_input("phone", phone)
            if not is_valid:
                print(f"Error: {error_message}")
                return

            for contact in contacts:
                contact_fields = contact.split("|")
                existing_name, _, existing_phone, _, _ = contact_fields

                if existing_phone == phone:
                    print(f"Contact found: {existing_name} ({existing_phone})")
                    confirmation = input("Do you want to delete this contact? (y/n): ").strip().lower()
                    if confirmation == 'y':
                        contacts.remove(contact)
                        print(f"Contact for '{existing_name}' has been deleted.")
                        save_contacts(contacts)
                    else:
                        print("Contact deletion cancelled.")
                    return
        
            print("Error: Phone number not found.")
        else:
            print("Invalid choice. Please try again.")