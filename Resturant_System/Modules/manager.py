import os

ordersFile = "./user_database/orders.txt"
menuFile = "./user_database/menu.txt"
feedbackFile = "./user_database/feedback.txt"

# Helper function to read from a file
def readFile(filePath):
    """Helper function to read content from a file."""
    try:
        with open(filePath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {filePath} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading {filePath}: {e}")
        return []

# Helper function to write to a file
def writeFile(filePath, data):
    """Helper function to write content to a file."""
    try:
        with open(filePath, "w") as file:
            file.writelines(data)
    except Exception as e:
        print(f"An unexpected error occurred while writing to {filePath}: {e}")

# Order Management
def viewOrders():
    """View all orders."""
    print("<-------- Orders List -------->")
    orders = readFile(ordersFile)
    if orders:
        for order in orders:
            print(order.strip())
    else:
        print("No orders available.")

def updateOrderStatus():
    """Update order status."""
    orderId = input("Enter order ID to update: ")
    status = input("Enter new status (Pending/In Progress/Completed): ")

    # Validate status input
    if status not in ["Pending", "In Progress", "Completed"]:
        print("Invalid status. Please choose from 'Pending', 'In Progress', or 'Completed'.")
        return

    orders = readFile(ordersFile)
    updatedOrders = []
    found = False

    for order in orders:
        orderDetails = order.strip().split(",")
        if orderDetails[0] == orderId:
            orderDetails[-1] = status
            found = True
        updatedOrders.append(",".join(orderDetails) + "\n")

    if found:
        writeFile(ordersFile, updatedOrders)
        print("Order status updated successfully.")
    else:
        print("Order not found.")

# Menu Management
def viewMenu():
    """View the restaurant menu."""
    print("<-------- Menu -------->")
    menuItems = readFile(menuFile)
    if menuItems:
        for item in menuItems:
            print(item.strip())
    else:
        print("No menu items available.")

def addMenuItem():
    """Add a new dish to the menu."""
    dishName = input("Enter dish name: ")
    try:
        price = float(input("Enter price: "))
        with open(menuFile, "a") as file:
            file.write(f"{dishName},{price}\n")
        print("Dish added successfully.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def removeMenuItem():
    """Remove a dish from the menu."""
    dishName = input("Enter dish name to remove: ")
    menuItems = readFile(menuFile)
    updatedMenu = []
    found = False

    for item in menuItems:
        if item.strip().split(",")[0] != dishName:
            updatedMenu.append(item)
        else:
            found = True

    if found:
        writeFile(menuFile, updatedMenu)
        print("Dish removed successfully.")
    else:
        print("Dish not found.")

# Sales Report
def viewSalesReport():
    """View sales report."""
    print("<-------- Sales Report -------->")
    totalSales = 0
    orders = readFile(ordersFile)

    for line in orders:
        details = line.strip().split(",")
        if len(details) >= 4:
            try:
                totalSales += float(details[3])  # Assuming price is the 4th value
            except ValueError:
                print(f"Invalid price data found for order: {line.strip()}")

    print(f"Total Sales: ${totalSales:.2f}")

# Customer Feedback
def viewFeedback():
    """View customer feedback."""
    print("<-------- Customer Feedback -------->")
    feedbacks = readFile(feedbackFile)
    if feedbacks:
        for feedback in feedbacks:
            print(feedback.strip())
    else:
        print("No feedback available.")

def menu():
    """Manager Menu"""
    while True:
        print("<-------- Manager Menu -------->")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. View Menu")
        print("4. Add Menu Item")
        print("5. Remove Menu Item")
        print("6. View Sales Report")
        print("7. View Customer Feedback")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            viewOrders()
        elif choice == "2":
            updateOrderStatus()
        elif choice == "3":
            viewMenu()
        elif choice == "4":
            addMenuItem()
        elif choice == "5":
            removeMenuItem()
        elif choice == "6":
            viewSalesReport()
        elif choice == "7":
            viewFeedback()
        elif choice == "8":
            print("Exiting Manager Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
