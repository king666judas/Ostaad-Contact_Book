import os

# Define the path for the contacts file
CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.csv")

def load_contacts():
    """Load contacts from the CSV file."""
    if not os.path.exists(CONTACTS_FILE):
        # Create an empty contacts file if it doesn't exist
        with open(CONTACTS_FILE, "w") as file:
            file.write("")
        return []

    with open(CONTACTS_FILE, "r") as file:
        return [line.strip() for line in file if line.strip()]

def save_contacts(contacts):
    """Save contacts to the CSV file."""
    try:
        # Open the file in write mode and overwrite its contents
        with open(CONTACTS_FILE, "w") as file:
            for contact in contacts:
                file.write(contact + "\n")  # Write each contact on a new line
        print("Contacts saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving contacts: {e}")
