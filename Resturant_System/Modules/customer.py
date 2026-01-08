import os

# File paths
customerFile = "./user_database/customer.txt"
menuFile = "./user_database/menu.txt"
orderFile = "./user_database/orders.txt"
feedbackFile = "./user_database/feedback.txt"

def customerMenu():
    """Display the menu for customers."""
    print("\n<-------- Menu -------->")
    if not os.path.exists(menuFile) or os.stat(menuFile).st_size == 0:
        print("No menu items available.")
        return

    try:
        with open(menuFile, "r") as file:
            for line in file:
                menuItem = line.strip().split(",")

                # Ensure correct format (dish, price, category)
                if len(menuItem) < 3:
                    continue  

                dish, price, category = menuItem
                print(f"{dish} - RM{price} ({category})")
    except Exception as e:
        print(f"Error reading menu file: {e}")

def placeOrder(customerName):
    """Allow customers to place an order."""
    print("\n<-------- Place Order -------->")
    
    if not os.path.exists(menuFile) or os.stat(menuFile).st_size == 0:
        print("No menu items available to order.")
        return

    orders = []
    availableDishes = set()

    try:
        # Read available dishes
        with open(menuFile, "r") as file:
            for line in file:
                menuItem = line.strip().split(",")
                if len(menuItem) >= 3:
                    availableDishes.add(menuItem[0].lower())  # Store dish names in lowercase for comparison

    except Exception as e:
        print(f"Error reading menu file: {e}")
        return

    while True:
        customerMenu()  # Show menu before ordering
        dish = input("Enter the dish you want to order (or type 'done' to finish): ").strip()

        if dish.lower() == "done":
            break

        if dish.lower() not in availableDishes:
            print("Invalid dish. Please select from the menu.")
            continue

        quantity = input("Enter quantity: ").strip()

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity. Please enter a positive number.")
            continue

        orders.append(f"{customerName},{dish},{quantity},Pending")

    if orders:
        try:
            with open(orderFile, "a") as file:
                for order in orders:
                    file.write(order + "\n")
            print("Order placed successfully!")
        except Exception as e:
            print(f"Error saving order: {e}")
    else:
        print("No items selected.")

def viewOrders(customerName):
    """Allow customers to view their past orders."""
    print("\n<-------- Your Orders -------->")
    if not os.path.exists(orderFile) or os.stat(orderFile).st_size == 0:
        print("No orders found.")
        return

    try:
        with open(orderFile, "r") as file:
            found = False
            for line in file:
                orderDetails = line.strip().split(",")

                # Ensure correct format (customer, dish, quantity, status)
                if len(orderDetails) < 4:
                    continue  

                storedCustomer, dish, quantity, status = orderDetails

                if storedCustomer.lower() == customerName.lower():
                    print(f"{dish} - {quantity} (Status: {status})")
                    found = True

            if not found:
                print("No orders found for you.")
    except Exception as e:
        print(f"Error reading orders file: {e}")

def provideFeedback(customerName):
    """Allow customers to provide feedback."""
    print("\n<-------- Provide Feedback -------->")
    feedback = input("Enter your feedback: ").strip()

    if not feedback:
        print("Feedback cannot be empty.")
        return

    try:
        with open(feedbackFile, "a") as file:
            file.write(f"{customerName},{feedback}\n")
        print("Thank you for your feedback!")
    except Exception as e:
        print(f"Error saving feedback: {e}")

def menu(customerName):
    """Customer menu options."""
    while True:
        print("\n<-------- Customer Menu -------->")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Your Orders")
        print("4. Provide Feedback")
        print("5. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            customerMenu()
        elif choice == "2":
            placeOrder(customerName)
        elif choice == "3":
            viewOrders(customerName)
        elif choice == "4":
            provideFeedback(customerName)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
