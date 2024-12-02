def validate_input(input_type, value):
    """
    Validates input based on the type specified.
    
    Parameters:
    - input_type (str): The type of input to validate ("name", "phone", "email", "address").
    - value (str): The input value to validate.
    
    Returns:
    - (bool, str): A tuple where the first value is True if valid, False otherwise, and 
                   the second value is an error message if invalid.
    """
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