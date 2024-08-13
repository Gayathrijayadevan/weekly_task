from users import *
from account_activities import*
from admin import*

DIRECTORY_PATH = "user_accounts"

if not os.path.exists(DIRECTORY_PATH):
    os.makedirs(DIRECTORY_PATH)

while True:
    print("\nWelcome to the Bank system")
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
                print("1. Create Account")
                print("2. Display Account")
                print("3. Deposit ")
                print("4. withdraw")
                print("5. Logout")

                ch = input("Enter your choice: ")

                if ch == '1':
                    create_account(DIRECTORY_PATH)
                
                elif ch == '2':
                    display_accounts(DIRECTORY_PATH)
                
                elif ch == '3':
                    username=input("Enter account holders name:")
                    acc_num=input("Enter account number:")
                    dep_amount=float(input("Enter amount your depositing:"))
                    deposit(DIRECTORY_PATH,username,acc_num,dep_amount)
                elif ch == '4':
                    w_username=input("Enter account holders name:")
                    acc_num=input("Enter account number:")
                    with_amount=float(input("Enter amount you wish to withdraw:"))
                    withdraw(DIRECTORY_PATH,w_username,acc_num,with_amount)
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
                print("1. View All Users")
                print("2.exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    admin_view_all_users(DIRECTORY_PATH) 
                elif admin_choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid admin credentials. Please try again.")

    elif choice == '4':
        print("Exiting  from Bank system")
        break

    else:
        print("Invalid choice. Please try again.")