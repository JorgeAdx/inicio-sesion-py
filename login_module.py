""" 
This module is a login system with preconfigured access credentials.
The username, password, and maximum number of login attempts can be
modified as needed.

The program will continue running until the user enters the correct
credentials or the maximum number of allowed attempts is reached.

Author: JorgeAdx
Date: 2025-09-22
"""
# --- Global configuration ---
REGISTERED_USER = "admin"
REGISTERED_PASSWORD = "1234"
MAX_ATTEMPTS = 3

def request_credentials():
    """Ask the user for username and password"""
    username = input("Username: ").strip()    # .strip() removes whitespaces
    password = input("Password: ").strip()
    return username, password

def validate_credentials(username, password):
    """Validate whether the credentials match those registered"""
    if username == REGISTERED_USER and password == REGISTERED_PASSWORD:
        return None    # Credentials match successfully
    return "Usuario o contraseña incorrectos.\n"

def manage_access_attempts(remaining_attempts):
    """ Show how many attempts are left or block access"""
    if remaining_attempts > 0:
        print(f"Remaining attempts: {remaining_attempts}\n")
    else:
        print("You have reached the maximum number of attempts. Access blocked.\n")

def login():
    """Define main function"""
    print("\n--- Login system ---")
    access_attempts = 0

    while access_attempts < MAX_ATTEMPTS:    # Loop until login succeeds or limit is reached
        username, password = request_credentials()

        # Validate empty fields without counting as an attempt
        if not username or not password: 
            print("Authentication error: Empty fields are not allowed.\n") 
            continue  # Prompt again without increasing the attempt counter
        
        # Validate credentials
        error = validate_credentials(username, password)
        if error:
            print(error)
            access_attempts += 1
            remaining_attempts = MAX_ATTEMPTS - access_attempts
            manage_access_attempts(remaining_attempts)
        else:
            print("Access granted. Welcome!\n")
            break

# Run main function
login()
