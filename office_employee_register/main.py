from user import *
from add import *
from display import *
from update import *
from delete import *
dtl=[]
while True:
    print("\nWelcome to employee register")
    print("1. Register")
    print("2. Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter Username: ")
        password = input("Set a Password: ")
        if register_user(username, password):
            print("Registration successful!")
        else:
            print("Username already exists.")
    
    elif choice == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if login_user(username, password):
            print("Login successful!")
            while True:
                print("1.Add Employee Details \n 2.Display Detalis \n 3.Update Detalis \n 4.Delete Detalis \n 5.Exit")
                a=int(input("Enter your choice:"))
                if a ==1:
                    add_detalis(dtl)
                elif a == 2:
                    display_details(dtl) 
                elif a == 3:
                     update_details(dtl)  
                elif a== 4:
                    remove(dtl) 
                elif a==5:
                    break
    elif  choice == 3:
        admin_username = input("Enter Admin Username: ")
        admin_password = input("Enter Admin Password: ")
        
        if is_admin1(admin_username,admin_password):
            print("Admin login successful!")  
            while True:
                print("\nAdmin Panel")
                print("1. View All employee detalis")
                print("2. view activity log")
                print("3. Logout") 
                admin_choice = input("Enter your choice: ")
                if admin_choice == '1':
                    admin_view(dtl)

                elif admin_choice =='2':
                    view_activity_logs() 

                elif admin_choice == '3':
                    print("Admin logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid admin credentials. Please try again.")       
    elif choice == 4:
        print("Thank you for empolyee registration system!")
        break

    else:
        print("Invalid choice. Please try again.")             


