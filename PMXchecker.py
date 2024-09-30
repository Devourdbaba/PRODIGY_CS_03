import re

def check_password_strength(password):
    """Assesses the strength of a password based on various criteria.

    Args:
        password (str): The password to be evaluated.

    Returns:
        str: A message indicating the password's strength.
    """

    # Define criteria for a strong password
    length_criteria = 8
    uppercase_criteria = 1
    lowercase_criteria = 1
    number_criteria = 1
    special_char_criteria = 1

    # Check password length
    if len(password) < length_criteria:
        return "Password is too short."

    # Check for uppercase, lowercase, numbers, and special characters
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    number_count = sum(1 for char in password if char.isdigit())
    special_char_count = sum(1 for char in password if not char.isalnum())

    # Check if password contains only numbers or letters
    if (uppercase_count + lowercase_count == 0) or (number_count == 0):
        return "Password is weak."

    # Check if password contains both numbers and letters
    if (uppercase_count + lowercase_count > 0) and (number_count > 0):
        return "Password is strong."
    
    # Check if password contains both numbers and letters and special characters
    if (uppercase_count + lowercase_count > 0) and (number_count > 0) :
        return "Password is moderate!"

    # Check if password contains both numbers and letters and special characters
    if (uppercase_count + lowercase_count > 0) and (number_count > 0) and (special_char_count > 0):
        return "Password is very strong!"

    # Password meets basic criteria but lacks additional complexity
    return "Password is good for use."

# Get password from user
password = input("Enter your password: ")

# Check password strength and provide feedback
result = check_password_strength(password)
print(result) 