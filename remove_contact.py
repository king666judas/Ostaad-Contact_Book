def remove_contact(contacts):
    print("\n--- Remove Contact ---")
    phone = input("Enter the phone number of the contact to remove: ").strip()
    for contact in contacts:
        if phone == contact.split("|")[2]:  # Match phone number
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("No contact found with the given phone number.")