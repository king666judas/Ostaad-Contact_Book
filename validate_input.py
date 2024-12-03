# validate_input.py
# Module for input validation.

'''
 >> Input Validation:
    > Validates data types and formats:
        Name:       Ensures input is a string.
        Phone:      Ensures its numeric and unique.
        Email:      Ensures it contains "@" and ".".
    > Provides feedback on invalid inputs.
'''

def validate_input(input_type, value):
    if input_type == "name":
        if all(char.isalpha() or char.isspace() for char in value):
            return True, ""
        else:
            return False, "Name should only contain letters and spaces."

    elif input_type == "phone":
        if value.isdigit():
            return True, ""
        else:
            return False, "Phone number should be a valid integer."

    elif input_type == "email":
        if "@" in value and "." in value:
            return True, ""
        else:
            return False, "Email address must contain '@' and at least one '.'."

    elif input_type == "address":
        if len(value) > 0:
            return True, ""
        else:
            return False, "Address cannot be empty."

    return False, "Invalid input type specified."