def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

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