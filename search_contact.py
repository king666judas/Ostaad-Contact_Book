from validate_input import validate_input

def search_contact(contacts):
    while True:
        print("\n--- Search Contact ---")
        print("1. Search for a Contact")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "2":
            print("Returning to main menu...")
            break

        if choice == "1":
            query = input("Enter name, email, or phone to search: ").strip().lower()

            if query.isdigit():
                is_valid, error_message = validate_input("phone", query)
                if not is_valid:
                    print(f"Error: {error_message}")
                    return

            results = [contact for contact in contacts if query in contact.lower()]
    
            if results:
                print("\n--- Search Results ---")
                for contact in results:
                    name, email, phone, address, photo = contact.split("|")
                    print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}, Photo: {photo}")
            else:
                print("No matching contacts found.")
        else:
            print("Invalid choice. Please try again.")