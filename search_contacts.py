from validate_input import validate_input

def search_contacts(contacts):
    """Search for a contact and display results in a table format."""
    if not contacts:
        print("\nNo contacts available to search.")
        return

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
        return

    # Get the corresponding field based on user choice
    field_map = {"1": "name", "2": "email", "3": "phone", "4": "address"}
    field_type = field_map.get(choice)
    if not field_type:
        print("Invalid choice. Please try again.")
        return

    query = input(f"Enter {field_type.capitalize()} to search: ").strip()

    # Validate input
    is_valid, error_message = validate_input(field_type, query)
    if not is_valid:
        print(f"Error: {error_message}")
        return

    # Find matching contacts
    matching_contacts = [
        contact.split("|") for contact in contacts if query.lower() in contact.lower()
    ]

    if not matching_contacts:
        print(f"\nNo contacts found matching '{query}'.")
        return

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