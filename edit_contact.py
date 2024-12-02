from validate_input import validate_input
from utilities import save_contacts

def edit_contact(contacts):
    while True:
        print("\n--- Edit Contact ---")
        print("1. Edit an Existing Contact")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "2":
            print("Returning to main menu...")
            break

        if choice == "1":
            phone = input("Enter phone number of the contact to edit: ").strip()

            # Validate the phone number
            is_valid, error_message = validate_input("phone", phone)
            if not is_valid:
                print(f"Error: {error_message}")
                return

            # Find the contact with the provided phone number
            contact_found = None
            for contact in contacts:
                contact_fields = contact.split("|")
                existing_name, existing_email, existing_phone, existing_name, existing_email, = contact_fields

                if existing_phone == phone:
                    contact_found = contact_fields
                    break

            if contact_found:
                print(f"Contact found: {contact_found[0]} ({contact_found[2]})")
                print(f"Current details: Name: {contact_found[0]}, Email: {contact_found[1]}, Address: {contact_found[3]}")

                # Allow the user to edit fields
                while True:
                    name = input(f"Enter new Name (current: {contact_found[0]}): ").strip() or contact_found[0]
                    is_valid, error_message = validate_input("name", name)
                    if not is_valid:
                        print(f"Error: {error_message}")
                        continue
                    break

                while True:
                    email = input(f"Enter new Email (current: {contact_found[1]}): ").strip() or contact_found[1]
                    is_valid, error_message = validate_input("email", email)
                    if not is_valid:
                        print(f"Error: {error_message}")
                        continue
                    break

                while True:
                    phone = input(f"Enter new Phone (current: {contact_found[2]}): ").strip() or contact_found[2]
                    is_valid, error_message = validate_input("phone", phone)
                    if not is_valid:
                        print(f"Error: {error_message}")
                        continue
                    break

                address = input(f"Enter new Address (current: {contact_found[3]}): ").strip() or contact_found[3]

                updated_contact = f"{name}|{email}|{phone}|{address}|{contact_found[4]}"

                # Replace the old contact with the updated one
                for i, contact in enumerate(contacts):
                    if contact.split("|")[2] == phone:  # Using phone number as identifier
                        contacts[i] = updated_contact
                        break

                print(f"Contact for {name} updated successfully!")
                
                save_contacts(contacts)  # Save updated contacts to the file
                break
            else:
                print("Contact with the provided phone number not found.")
        else:
            print("Invalid choice. Please try again.")