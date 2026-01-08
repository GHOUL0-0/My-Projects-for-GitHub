"""
Admin Credentials
This file contains the admin credentials for the restaurant management system.
This is a simple version suitable for first-year students.
"""

# Simple admin credentials (for learning purposes)
ADMIN_NAME = "Admin"
ADMIN_EMAIL = "admin@restaurant.com"
ADMIN_PHONE = "1234567890"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Dictionary to store admin information
ADMIN_CREDENTIALS = {
    "name": ADMIN_NAME,
    "email": ADMIN_EMAIL,
    "phone": ADMIN_PHONE,
    "username": ADMIN_USERNAME,
    "password": ADMIN_PASSWORD
}

def check_admin_login(username: str, password: str) -> bool:
    """
    Simple function to check if the login credentials match the admin credentials.
    This is a basic version for learning purposes.
    """
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def update_admin_info(new_name: str, new_email: str, new_phone: str, new_username: str, new_password: str) -> None:
    """
    Simple function to update admin information.
    This is a basic version for learning purposes.
    """
    global ADMIN_NAME, ADMIN_EMAIL, ADMIN_PHONE, ADMIN_USERNAME, ADMIN_PASSWORD
    
    ADMIN_NAME = new_name
    ADMIN_EMAIL = new_email
    ADMIN_PHONE = new_phone
    ADMIN_USERNAME = new_username
    ADMIN_PASSWORD = new_password
    
    # Update the dictionary as well
    ADMIN_CREDENTIALS.update({
        "name": new_name,
        "email": new_email,
        "phone": new_phone,
        "username": new_username,
        "password": new_password
    })

    