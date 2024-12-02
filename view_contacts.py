def view_contacts(contacts):
    """Display all contacts in a neatly formatted table."""
    if not contacts:
        print("\nNo contacts available to display.")
        return

    # Split contacts into fields for formatting
    contact_data = [contact.split("|") for contact in contacts]

    # Define headers
    headers = ["Name", "Email", "Phone", "Address", "Photo"]
    
    # Calculate the maximum width for each column
    column_widths = [len(header) for header in headers]
    for contact in contact_data:
        for i, field in enumerate(contact):
            column_widths[i] = max(column_widths[i], len(field))

    # Create a row formatter based on column widths
    row_format = " | ".join([f"{{:<{width}}}" for width in column_widths])

    # Print the header row
    print("\n" + "=" * (sum(column_widths) + len(column_widths) * 3 - 1))
    print(row_format.format(*headers))
    print("=" * (sum(column_widths) + len(column_widths) * 3 - 1))

    # Print each contact
    for contact in sorted(contact_data, key=lambda x: x[0].lower()):  # Sort by name
        print(row_format.format(*contact))

    print("=" * (sum(column_widths) + len(column_widths) * 3 - 1))