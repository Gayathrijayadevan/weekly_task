from menu import display_menu, get_item,admin_add,admin_delete
from orders import create_order, view_orders, cancel_order
from users import register_user, login_user, current_user, logout_user, is_admin1

while True:
    print("\nWelcome to the Food Ordering System")
    print("1. Register")
    print("2. Login")
    print("3. Admin Login")
    print("4. Exit")

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
            print("Login successful!")
            while True:
                print(f"\nWelcome, {username}")
                print("1. Display Menu")
                print("2. Place Order")
                print("3. View Orders")
                print("4. Cancel Order")
                print("5. Logout")

                ch = input("Enter your choice: ")

                if ch == '1':
                    display_menu()
                
                elif ch == '2':
                    item_id = input("Enter the item ID to order: ")
                    quantity = int(input("Enter the quantity: "))
                    item = get_item(item_id)
                    if item:
                        create_order(username, item, quantity)
                        print("Order placed successfully!")
                    else:
                        print("Invalid item ID.")
                
                elif ch == '3':
                    print(current_user)
                    view_orders(username)
                
                elif ch == '4':
                    order_id = input("Enter the order ID to cancel: ")
                    if cancel_order(order_id, username):
                        print("Order cancelled successfully!")
                    else:
                        print("Order not found or you don't have permission to cancel this order.")
                
                elif ch == '5':
                    logout_user()
                    print("Logged out successfully.")
                    break  
                
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid username or password. Please try again.")

    elif choice == '3':
        admin_username = input("Enter Admin Username: ")
        admin_password = input("Enter Admin Password: ")
        
        if is_admin1(admin_username,admin_password):
            print("Admin login successful!")
            while True:
                print("\nAdmin Panel")
                print("1. View All Orders")
                print("2. Add Item to Menu")
                print("3. Remove Item from Menu")
                print("4. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    view_orders()  
                elif admin_choice == '2':
                    admin_add()
                elif admin_choice == '3':
                    admin_delete()
                elif admin_choice == '4':
                    print("Admin logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid admin credentials. Please try again.")

    elif choice == '4':
        print("Thank you for using the Food Ordering System!")
        break

    else:
        print("Invalid choice. Please try again.")