def load_contacts():
    FILE_PATH = "contacts.csv"
    contacts = []
    try:
        with open(FILE_PATH, mode="r") as file:
            for line in file:
                contact = line.strip()  # Remove trailing newline characters
                if contact.count("|") == 4:  # Ensure correct number of fields
                    contacts.append(contact)
                else:
                    print(f"Skipped malformed contact: {contact}")
        print(f"Loaded {len(contacts)} contacts from file.")
    except FileNotFoundError:
        print("No contacts file found. Starting fresh.")
    return contacts