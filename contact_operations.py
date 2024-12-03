# contact_operations.py   
# Add, edit, search, remove functions.

from file_handler import save_contacts
from validate_input import validate_input

'''
> Add Contact:
    Collects validated data and adds a new contact.
    Checks for duplicate phone numbers before saving.
'''
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

'''
> Edit Contact:
    Allows users to modify existing contact details.
    Updates the CSV file after changes.
'''
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

'''
> Search Contact:
    Searches for contacts by name, email, phone, or address.
    Displays results in a tabular format.
'''
def search_contacts(contacts):
    """Search for a contact and display results in a table format."""
    if not contacts:
        print("\nNo contacts available to search.")
        return

    while True:
        # Ask user for input type
        print("\n--- Search Contacts ---")
        print("1. Search by Name")
        print("2. Search by Email")
        print("3. Search by Phone")
        print("4. Search by Address")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "5":
            print("Returning to main menu...")
            break

        # Map choice to the contact field
        field_map = {"1": "name", "2": "email", "3": "phone", "4": "address"}
        field_type = field_map.get(choice)
        if not field_type:
            print("Invalid choice. Please try again.")
            continue

        query = input(f"Enter {field_type.capitalize()} to search: ").strip()

        # Validate the input
        is_valid, error_message = validate_input(field_type, query)
        if not is_valid:
            print(f"Error: {error_message}")
            continue

        # Perform the search
        matching_contacts = [
            contact.split("|") for contact in contacts if query.lower() in contact.lower()
        ]

        if not matching_contacts:
            print(f"\nNo contacts found matching '{query}'.")
            continue

        # Define headers
        headers = ["Name", "Email", "Phone", "Address", "Photo"]

        # Calculate the maximum width for each column
        column_widths = [len(header) for header in headers]
        for contact in matching_contacts:
            for i, field in enumerate(contact):
                column_widths[i] = max(column_widths[i], len(field))

        # Create a row formatter based on column widths
        row_format = " | ".join([f"{{:<{width}}}" for width in column_widths])

        # Print the header row
        print("\nSearch Results:")
        print("=" * (sum(column_widths) + len(column_widths) * 3 - 1))
        print(row_format.format(*headers))
        print("=" * (sum(column_widths) + len(column_widths) * 3 - 1))

        # Print each matching contact
        for contact in matching_contacts:
            print(row_format.format(*contact))

        print("=" * (sum(column_widths) + len(column_widths) * 3 - 1))

'''
> Remove Contact:
    Deletes a contact by phone number.
    Confirms deletion and updates the CSV file.
'''
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