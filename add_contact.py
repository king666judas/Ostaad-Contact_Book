from utilities import save_contacts
from validate_input import validate_input

def add_contact(contacts):
    while True:
        print("\n--- Add Contact ---")
        print("1. Add a New Contact")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "2":
            print("Returning to main menu...")
            break

        if choice == "1":
            while True:
                name = input("Enter Name: ").strip()
                is_valid, error_message = validate_input("name", name)
                if not is_valid:
                    print(f"Error: {error_message}")
                    continue
                break

            while True:
                phone = input("Enter Phone Number: ").strip()
                is_valid, error_message = validate_input("phone", phone)
                if not is_valid:
                    print(f"Error: {error_message}")
                    continue
                # Check for duplicate phone numbers
                if any(phone in contact.split("|")[2] for contact in contacts):
                    print("Error: This phone number is already associated with another contact.")
                    continue
                break

            while True:
                email = input("Enter Email: ").strip()
                is_valid, error_message = validate_input("email", email)
                if not is_valid:
                    print(f"Error: {error_message}")
                    continue
                break

            address = input("Enter Address: ").strip()
            is_valid, error_message = validate_input("address", address)
            if not is_valid:
                print(f"Error: {error_message}")
                return

            # Check if phone number already exists in contacts
            for contact in contacts:
                contact_fields = contact.split("|")
                existing_name, _, existing_phone, _, _ = contact_fields

                if existing_phone == phone:  # Phone number already exists
                    if existing_name == name:
                        print(f"Error: This phone number is already associated with '{name}'.")
                    else:
                        print(f"Error: This phone number is already assigned to '{existing_name}'.")
                    return  # Exit without adding the contact

            # Add new contact
            contact = f"{name}|{email}|{phone}|{address}|NoPhoto"
            contacts.append(contact)
            print(f"Contact for '{name}' added successfully!")
            save_contacts(contacts)
        else:
            print("Invalid choice. Please try again.")