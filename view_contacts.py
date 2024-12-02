def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    
    print("\n--- View Contacts (Sorted Alphabetically) ---")
    
    # Sort contacts by name (first field)
    sorted_contacts = sorted(contacts, key=lambda contact: contact.split("|")[0])

    for contact in sorted_contacts:
        name, email, phone, address, photo = contact.split("|")
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}, Photo: {photo}")