"""
Restaurant Management System
This program manages a restaurant with different user roles:
- Admin: Can manage staff and system settings
- Manager: Can manage menu and orders
- Chef: Can view and update order status
- Customer: Can view menu and place orders
"""

from Modules import auth, admin, manager, chef, customer
import sys
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display a welcome message with a simple border"""
    clear_screen()
    print("\n" + "=" * 50)
    print("Welcome to Delicious Restaurant System")
    print("=" * 50 + "\n")

def main():
    try:
        # Display welcome message
        display_welcome()
        
        # Get user authentication result
        print("Please login or signup to continue...")
        result = auth.authMenu()
        
        # Check if authentication was successful
        if result is None or (isinstance(result, tuple) and result[0] is None):
            print("\nProgram terminated. Thank you for using our system!")
            return
        
        # Safely unpack the authentication result
        if isinstance(result, tuple) and len(result) == 2:
            user_role, user_name = result
            clear_screen()
            print(f"\nWelcome {user_name}!")
            
            # Direct users to their respective menus based on role
            role_menus = {
                "admin": admin.menu,
                "manager": manager.menu,
                "chef": chef.menu,
                "customer": lambda: customer.menu(user_name)
            }
            
            # Get and execute the appropriate menu function
            menu_function = role_menus.get(user_role)
            if menu_function:
                menu_function()
            else:
                print("Error: Invalid role detected. Please contact support.")
        else:
            print("Error: System could not process login information.")
            print("Please try again later.")
            
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Thank you for using our system!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Please try again later.")
    finally:
        print("\nGoodbye! Have a great day!")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
