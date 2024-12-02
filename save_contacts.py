def save_contacts(contacts):
    FILE_PATH = "contacts.csv"
    try:
        with open(FILE_PATH, mode="w") as file:
            for contact in contacts:
                file.write(contact + "\n")  # Write each contact as a line
        print("Contacts saved successfully!")
    except Exception as e:
        print(f"Error saving contacts: {e}")