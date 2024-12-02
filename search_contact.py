def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name, email, or phone to search: ").strip().lower()
    results = [contact for contact in contacts if query in contact.lower()]
    
    if results:
        print(f"Found {len(results)} result(s):")
        for result in results:
            name, email, phone, address, photo = result.split("|")
            print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}, Photo: {photo}")
    else:
        print("No matching contacts found.")