import re


def validate_user_details(email_address, mobile_number, user_password):
    """
    Validates the provided email, mobile number,
    and password against predefined patterns.

    :param email_address: The email address string to validate.
    :param mobile_number: The Indian mobile number string to validate.
    :param user_password: The password string to validate for strength.
    :raises ValueError: If any of the details fail validation.
    :return: A success message if all details are valid.
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mobile_pattern = r'^[6-9]\d{9}$'
    password_pattern = (
        r'^(?=.*[A-Z])'         # At least one uppercase letter
        r'(?=.*[a-z])'          # At least one lowercase letter
        r'(?=.*\d)'             # At least one digit
        r'(?=.*[@$!%*?&])'      # At least one special character
        r'[A-Za-z\d@$!%*?&]{8,}$'  # Minimum 8 characters, from allowed set
    )
    if not re.match(email_pattern, email_address):
        raise ValueError("Invalid email address")

    if not re.match(mobile_pattern, mobile_number):
        raise ValueError("Invalid Indian mobile number")

    if not re.match(password_pattern, user_password):
        raise ValueError("Password must be strong (at least 8 characters, "
                         "including an uppercase letter, a lowercase letter, "
                         "a digit, and a special character).")

    return "All details are valid"


try:
    print("User Registration Validation")

    # Renamed global variables to avoid W0621 warnings
    input_email = input("Enter email: ")
    input_mobile = input("Enter mobile number: ")
    input_password = input("Enter password: ")

    RESULT = validate_user_details(input_email, input_mobile, input_password)
    print(RESULT)

except ValueError as ve:
    print("Validation Error:", ve)

else:
    print("User registered successfully")

finally:
    print("\n--- REGISTRATION PROCESS ENDED ---")