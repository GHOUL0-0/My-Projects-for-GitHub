"""
Authentication Module
This module handles user authentication including login and signup functionality.
It supports different user roles: admin, manager, chef, and customer.
"""

import os
import re
from user_database.admin_credentials import ADMIN_NAME, ADMIN_EMAIL, ADMIN_PHONE, ADMIN_USERNAME, ADMIN_PASSWORD

# File paths for storing user data
userFile = "./user_database/users.txt"
customerFile = "./user_database/customer.txt"

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_email(email):
    """Check if email format is valid"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Check if phone number format is valid"""
    pattern = r'^\d{10}$'  # Assumes 10-digit phone number
    return re.match(pattern, phone) is not None

def validate_password(password):
    """Check if password meets minimum requirements"""
    if len(password) < 4:
        return False, "Password must be at least 4 characters long"
    return True, "Password is valid"

def checkCredentials(filePath, username, password):
    """Verify user credentials from file"""
    try:
        if not os.path.exists(filePath):
            print(f"Error: User database not found.")
            return None
            
        with open(filePath, "r") as file:
            for line in file:
                if line.startswith('#'):  # Skip header lines
                    continue
                data = line.strip().split(",")
                if len(data) != 5:  # Ensure data format is correct
                    continue
                    
                storedName, storedEmail, storedPhone, storedPassword, storedRole = data
                if username == storedName and password == storedPassword:
                    return storedRole, storedName
    except Exception as e:
        print(f"Error accessing user database: {str(e)}")
    return None

def login():
    """Handle user login with proper error messages"""
    attempts = 3
    print("\n" + "=" * 30)
    print("Login to Your Account")
    print("=" * 30)

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("Error: Username and password cannot be empty!")
            attempts -= 1
            continue

        # Check admin login
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\nWelcome Admin! Access granted.")
            return "admin", username

        # Check staff login
        staff_result = checkCredentials(userFile, username, password)
        if staff_result:
            role, name = staff_result
            print(f"\nWelcome {name}! You are logged in as {role}.")
            return role, name

        # Check customer login
        customer_result = checkCredentials(customerFile, username, password)
        if customer_result:
            role, name = customer_result
            print(f"\nWelcome {name}! You are logged in as {role}.")
            return role, name

        attempts -= 1
        print(f"\nError: Invalid username or password.")
        
    print("\nToo many failed attempts. Please try again later.")
    return None, None

def signup():
    """Handle user registration"""
    print("\n" + "=" * 30)
    print("Create New Account")
    print("=" * 30)
    print("\n1. Staff Registration")
    print("2. Customer Registration")
    print("3. Go Back")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == "1":
                return signupStaff()
            elif choice == "2":
                return signupCustomer()
            elif choice == "3":
                print("\nReturning to main menu...")
                return None
            else:
                print("Error: Please enter 1, 2, or 3")
        except ValueError:
            print("Error: Invalid input")

def signupStaff():
    """Register new staff member with validation"""
    print("\n" + "=" * 30)
    print("Staff Registration")
    print("=" * 30)

    # Admin verification
    print("\nAdmin verification required:")
    adminUsername = input("Admin Username: ").strip()
    adminPassword = input("Admin Password: ").strip()

    if adminUsername != ADMIN_USERNAME or adminPassword != ADMIN_PASSWORD:
        print("\nError: Admin verification failed!")
        return None

    # Get staff information with validation
    while True:
        name = input("\nStaff Name: ").strip()
        if len(name) < 2:
            print("Error: Name must be at least 2 characters long")
            continue

        email = input("Email: ").strip()
        if not validate_email(email):
            print("Error: Invalid email format")
            continue

        phone = input("Phone (10 digits): ").strip()
        if not validate_phone(phone):
            print("Error: Invalid phone number format")
            continue

        password = input("Password: ").strip()
        is_valid, msg = validate_password(password)
        if not is_valid:
            print(f"Error: {msg}")
            continue

        role = input("Role (manager/chef): ").strip().lower()
        if role not in ["manager", "chef"]:
            print("Error: Role must be either 'manager' or 'chef'")
            continue

        break

    # Save staff information
    try:
        with open(userFile, "a") as file:
            file.write(f"{name},{email},{phone},{password},{role}\n")
        print(f"\nSuccess! {name} has been registered as {role}.")
    except Exception as e:
        print(f"\nError registering staff: {str(e)}")

def signupCustomer():
    """Register new customer with validation"""
    print("\n" + "=" * 30)
    print("Customer Registration")
    print("=" * 30)

    while True:
        name = input("\nYour Name: ").strip()
        if len(name) < 2:
            print("Error: Name must be at least 2 characters long")
            continue

        email = input("Email: ").strip()
        if not validate_email(email):
            print("Error: Invalid email format")
            continue

        phone = input("Phone (10 digits): ").strip()
        if not validate_phone(phone):
            print("Error: Invalid phone number format")
            continue

        password = input("Password: ").strip()
        is_valid, msg = validate_password(password)
        if not is_valid:
            print(f"Error: {msg}")
            continue

        break

    try:
        with open(customerFile, "a") as file:
            file.write(f"{name},{email},{phone},{password},customer\n")
        print("\nRegistration successful! You can now login as a customer.")
    except Exception as e:
        print(f"\nError during registration: {str(e)}")

def authMenu():
    """Display and handle authentication menu"""
    while True:
        print("\n" + "=" * 30)
        print("Authentication Menu")
        print("=" * 30)
        print("\n1. Login")
        print("2. Sign Up")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            result = login()
            if result[0]:  # If login successful
                return result
        elif choice == "2":
            signup()
        elif choice == "3":
            print("\nThank you for using our system!")
            return None, None
        else:
            print("Error: Please enter 1, 2, or 3")
