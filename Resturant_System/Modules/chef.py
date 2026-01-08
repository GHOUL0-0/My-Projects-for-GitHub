import os

# File paths
orderFile = "./user_database/orders.txt"
feedbackFile = "./user_database/feedback.txt"

def viewOrders():
    """Displays all pending or in-progress orders assigned to the chef."""
    if not os.path.exists(orderFile):
        print("No orders available.")
        return
    
    print("\n<------ Pending & In-Progress Orders ------>")
    found = False

    try:
        with open(orderFile, "r") as file:
            for line in file:
                orderDetails = line.strip().split(",")
                
                # Ensure proper order format
                if len(orderDetails) < 4:
                    continue

                customerName, items, total, status = orderDetails[:4]

                if status in ["Pending", "In Progress"]:
                    print(f"Customer: {customerName} | Items: {items} | Total: RM{total} | Status: {status}")
                    found = True

    except Exception as e:
        print(f"Error reading orders file: {e}")
    
    if not found:
        print("No orders require attention.")

def updateOrderStatus():
    """Allows the chef to update the status of an order."""
    if not os.path.exists(orderFile):
        print("No orders available.")
        return
    
    try:
        with open(orderFile, "r") as file:
            orders = [line.strip().split(",") for line in file]

        if not orders:
            print("No orders found.")
            return

        print("\n<------ Update Order Status ------>")
        customerName = input("Enter the customer's name for the order you want to update: ").strip()
        updated = False

        for order in orders:
            if len(order) >= 4 and order[0] == customerName and order[3] in ["Pending", "In Progress"]:
                print(f"Current Status: {order[3]}")
                newStatus = input("Enter new status [In Progress / Ready for Pickup]: ").strip().title()
                
                if newStatus in ["In Progress", "Ready For Pickup"]:
                    order[3] = newStatus
                    updated = True
                    break
                else:
                    print("Invalid status entered. Please enter 'In Progress' or 'Ready for Pickup'.")
                    return

        if updated:
            with open(orderFile, "w") as file:
                for updatedOrder in orders:
                    file.write(",".join(updatedOrder) + "\n")
            print(f"Order status updated to {newStatus} for {customerName}.")
        else:
            print("Order not found or already completed.")

    except Exception as e:
        print(f"Error updating order: {e}")

def viewFeedback():
    """Allows the chef to view customer feedback related to food quality."""
    if not os.path.exists(feedbackFile):
        print("No feedback available.")
        return
    
    print("\n<------ Customer Feedback ------>")
    try:
        with open(feedbackFile, "r") as file:
            feedbacks = file.readlines()
        
        if not feedbacks:
            print("No feedback received yet.")
            return
        
        for feedback in feedbacks:
            feedbackDetails = feedback.strip().split(",", 1)

            # Ensure feedback is properly formatted
            if len(feedbackDetails) < 2:
                continue

            customerName, feedbackText = feedbackDetails
            print(f"{customerName}: {feedbackText}")

    except Exception as e:
        print(f"Error reading feedback file: {e}")

def menu():
    """Chef Menu"""
    while True:
        print("\n<------ Chef Menu ------>")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. View Customer Feedback")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            viewOrders()
        elif choice == "2":
            updateOrderStatus()
        elif choice == "3":
            viewFeedback()
        elif choice == "4":
            print("Logging out. Goodbye, Chef!")
            break
        else:
            print("Invalid choice. Please try again.")
