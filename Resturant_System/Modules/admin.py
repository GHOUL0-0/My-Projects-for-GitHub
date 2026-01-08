import os
from user_database import admin_credentials

# File paths
staffFile = "./user_database/users.txt"
ordersFile = "./user_database/orders.txt"
feedbackFile = "./user_database/feedback.txt"

def viewSalesReport():
    """View sales report based on month or chef."""
    print("<-------- Sales Report -------->")
    criteria = input("Enter criteria (month, chef): ").strip().lower()

    if criteria == "month":
        month = input("Enter month (YYYY-MM format): ").strip()
        totalSales = 0

        try:
            with open(ordersFile, "r") as file:
                for line in file:
                    orderId, customerName, dish, price, chef, orderDate = line.strip().split(",")
                    if month in orderDate:
                        totalSales += float(price)
            print(f"Total sales for {month}: ${totalSales:.2f}")
        except FileNotFoundError:
            print("Error: Orders file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif criteria == "chef":
        chefName = input("Enter chef name: ").strip()
        totalSales = 0

        try:
            with open(ordersFile, "r") as file:
                for line in file:
                    orderId, customerName, dish, price, chef, orderDate = line.strip().split(",")
                    if chefName.lower() == chef.lower():
                        totalSales += float(price)
            print(f"Total sales for {chefName}: ${totalSales:.2f}")
        except FileNotFoundError:
            print("Error: Orders file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid criteria. Please enter 'month' or 'chef'.")

def viewFeedback():
    """View customer feedback."""
    print("<-------- Customer Feedback -------->")
    try:
        with open(feedbackFile, "r") as file:
            feedbacks = file.readlines()
            if feedbacks:
                for feedback in feedbacks:
                    print(feedback.strip())
            else:
                print("No feedback available.")
    except FileNotFoundError:
        print("Error: Feedback file not found.")

def manageStaff():
    """Add, edit, or delete staff members."""
    print("<-------- Manage Staff -------->")
    print("1. Add Staff")
    print("2. Edit Staff")
    print("3. Delete Staff")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        addStaff()
    elif choice == "2":
        editStaff()
    elif choice == "3":
        deleteStaff()
    else:
        print("Invalid choice. Please try again.")

def addStaff():
    """Add a new staff member."""
    print("<-------- Add Staff -------->")
    name = input("Enter staff name: ").strip()
    email = input("Enter staff email: ").strip()
    phone = input("Enter staff phone number: ").strip()
    password = input("Enter staff password: ").strip()
    role = input("Enter staff role [manager/chef]: ").strip().lower()

    if role not in ["manager", "chef"]:
        print("Invalid role. Please enter 'manager' or 'chef'.")
        return

    try:
        with open(staffFile, "a") as file:
            file.write(f"{name},{email},{phone},{password},{role}\n")
        print(f"{name} has been added as a {role}.")
    except Exception as e:
        print(f"Error adding staff: {e}")

def editStaff():
    """Edit an existing staff member."""
    print("<-------- Edit Staff -------->")
    name = input("Enter staff name to edit: ").strip()
    found = False

    try:
        with open(staffFile, "r") as file:
            lines = file.readlines()

        with open(staffFile, "w") as file:
            for line in lines:
                storedName, email, phone, password, role = line.strip().split(",")
                if storedName.lower() == name.lower():
                    found = True
                    newName = input(f"Enter new name for {name} (leave empty to keep current): ").strip() or storedName
                    newEmail = input(f"Enter new email for {name} (leave empty to keep current): ").strip() or email
                    newPhone = input(f"Enter new phone for {name} (leave empty to keep current): ").strip() or phone
                    newPassword = input(f"Enter new password for {name} (leave empty to keep current): ").strip() or password
                    file.write(f"{newName},{newEmail},{newPhone},{newPassword},{role}\n")
                    print(f"Staff {name} updated successfully.")
                else:
                    file.write(line)
        if not found:
            print(f"Staff {name} not found.")
    except FileNotFoundError:
        print("Error: Staff file not found.")

def deleteStaff():
    """Delete an existing staff member."""
    print("<-------- Delete Staff -------->")
    name = input("Enter staff name to delete: ").strip()
    found = False

    try:
        with open(staffFile, "r") as file:
            lines = file.readlines()

        with open(staffFile, "w") as file:
            for line in lines:
                storedName, email, phone, password, role = line.strip().split(",")
                if storedName.lower() == name.lower():
                    found = True
                    print(f"Staff {name} deleted successfully.")
                    continue
                file.write(line)
        if not found:
            print(f"Staff {name} not found.")
    except FileNotFoundError:
        print("Error: Staff file not found.")

def updateProfile():
    """Update the admin's profile."""
    print("<-------- Update Profile -------->")
    
    newName = input(f"Enter new name (Current: {admin_credentials.ADMIN_NAME}): ").strip() or admin_credentials.ADMIN_NAME
    newEmail = input(f"Enter new email (Current: {admin_credentials.ADMIN_EMAIL}): ").strip() or admin_credentials.ADMIN_EMAIL
    newPhone = input(f"Enter new phone (Current: {admin_credentials.ADMIN_PHONE}): ").strip() or admin_credentials.ADMIN_PHONE
    newUsername = input(f"Enter new username (Current: {admin_credentials.ADMIN_USERNAME}): ").strip() or admin_credentials.ADMIN_USERNAME
    newPassword = input("Enter new password (leave blank to keep current): ").strip() or admin_credentials.ADMIN_PASSWORD

    updateAdminCredentials(newName, newEmail, newPhone, newUsername, newPassword)
    print("Profile updated successfully!")

def updateAdminCredentials(name, email, phone, username, password):
    """Update the admin credentials file."""
    credentialsPath = "./user_database/admin_credentials.py"

    newContent = f"""# Store admin credentials
ADMIN_NAME = "{name}"
ADMIN_EMAIL = "{email}"
ADMIN_PHONE = "{phone}"
ADMIN_USERNAME = "{username}"
ADMIN_PASSWORD = "{password}"
"""

    try:
        with open(credentialsPath, "w") as file:
            file.write(newContent)
    except Exception as e:
        print(f"Error updating admin credentials: {e}")

def menu():
    """Admin Menu"""
    while True:
        print("\n<-------- Admin Menu -------->")
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Feedback")
        print("4. Update Profile")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manageStaff()
        elif choice == "2":
            viewSalesReport()
        elif choice == "3":
            viewFeedback()
        elif choice == "4":
            updateProfile()
        elif choice == "5":
            print("Exiting Admin Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
