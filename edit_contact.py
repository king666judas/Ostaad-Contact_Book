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
                continue

            # Find the contact by phone number
            contact_found = None
            for index, contact in enumerate(contacts):
                contact_fields = contact.split("|")
                if contact_fields[2] == phone:  # Match by phone number
                    contact_found = (index, contact_fields)
                    break

            if contact_found:
                index, fields = contact_found
                name, email, phone, address, photo = fields

                print(f"Editing Contact: {name} ({phone})")
                print("Leave fields blank to keep current values.")

                # Get updated fields
                new_name = input(f"New Name (current: {name}): ").strip() or name
                new_email = input(f"New Email (current: {email}): ").strip() or email
                new_phone = input(f"New Phone (current: {phone}): ").strip() or phone
                new_address = input(f"New Address (current: {address}): ").strip() or address

                # Validate the inputs
                for field_name, field_value in [("name", new_name), ("email", new_email), ("phone", new_phone)]:
                    is_valid, error_message = validate_input(field_name, field_value)
                    if not is_valid:
                        print(f"Error: {error_message}")
                        return

                # Update the contact
                updated_contact = f"{new_name}|{new_email}|{new_phone}|{new_address}|{photo}"
                contacts[index] = updated_contact

                # Save the updated list to the file
                save_contacts(contacts)
                print("Contact updated successfully!")
            else:
                print("No contact found with that phone number.")
        else:
            print("Invalid choice. Try again.")