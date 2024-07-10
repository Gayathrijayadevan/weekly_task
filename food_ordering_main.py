from menu import display_menu, get_item
from orders import create_order, view_orders, cancel_order
from users import register_user, login_user, current_user, logout_user
while True:

        print("\nWelcome to the Food Ordering System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
                username = input("Enter Username: ")
                password = input("Set a Password: ")
                if register_user(username, password):
                    print("Registration successful!")
                else:
                    print("Username already exists.")
        elif choice == '2':
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if login_user(username, password):
                    print("Login successful!") #modified
                    while True:
                        print(f"\nWelcome, {current_user['username']}!")
                        print("1. Display Menu")
                        print("2. Place Order")
                        print("3. View Orders")
                        print("4. Cancel Order")
                        print("5. Logout")

            
                        if choice == '1':
                            display_menu()
                        elif choice == '2':
                            item_id = input("Enter the item ID to order: ")
                            quantity = int(input("Enter the quantity: "))
                            item = get_item(item_id)
                            if item:
                                create_order(current_user['username'], item, quantity)
                                print("Order placed successfully!")
                            else:
                                print("Invalid item ID.")
                        elif choice == '3':
                            view_orders(current_user['username'])
                        elif choice == '4':
                            order_id = input("Enter the order ID to cancel: ")
                            if cancel_order(order_id, current_user['username']):
                                print("Order cancelled successfully!")
                            else:
                                print("Order not found or you don't have permission to cancel this order.")
                        elif choice == '5':
                            logout_user()
                            print("Logged out successfully.")
                        else:
                            print("Invalid choice. Please try again.")
        elif choice == '3':
                print("Thank you for using the Food Ordering System!")
                break
        else:
                print("Invalid choice. Please try again.")

