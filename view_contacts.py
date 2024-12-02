def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    print("\n--- View Contacts ---")
    for contact in contacts:
        name, email, phone, address, photo = contact.split("|")
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}, Photo: {photo}")