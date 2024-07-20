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
                    display_detalis(dtl) 
                elif a == 3:
                    update_detalis(dtl)  
                elif a== 4:
                    remove(dtl)         

