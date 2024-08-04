
from admin import *
from product import*
from sales import *
from inventory import *
from employee import *
from customer import *
from suppiler import *

while True:
    print("\nWelcome to the mobileshop database")
    print("1. Admin Login")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        admin_username = input("Enter Admin Username: ")
        admin_password = input("Enter Admin Password: ")
        
        if is_admin1(admin_username,admin_password):
            print("Admin login successful!")
            while True:
                print("1.Add Detalis")
                print("2.Update Detalis")
                print(" 3.Delete Detalis")
                print(" 4.Display Details")
                print(" 5.Search Detalis ")
                print("6.Exit ")
                ch=(input("Enter your choice:"))
                if ch == '1':
                    while True:
                        print("which table would you like add the detalis to?")    
                        print("1.Product Table")
                        print("2.Customer Table")
                        print("3.Sales Table")
                        print("4.Suppiler Table")
                        print("5.Inventory Table")
                        print("6.Employee Table ")
                        print("7.Exit")
                        choi=(input("Enter your choice:"))
                        if choi==1:
                            add_product_details() 
                        elif choi == '2':
                            add_customer_details()
                        elif choi == '3':
                            add_sales_details()
                        elif choi == '4':
                            add_supplier_details()
                        elif choi =='5':
                            add_inventory_details()
                        elif choi=='6':
                            add_employee_details()    
                        elif choi =='7':
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif ch == '2':
                    while True:
                        print("which table would you like update the detalis?")    
                        print("1.Product Table")
                        print("2.Customer Table")
                        print("3.Sales Table")
                        print("4.Suppiler Table")
                        print("5.Inventory Table")
                        print("6.Employee Table ")
                        print("7.Exit")
                        choi=(input("Enter your choice:"))
                        if choi==1:
                            update_product_detalis() 
                        elif choi == '2':
                            update_customer_detalis()
                        elif choi == '3':
                            update_sales_detalis()
                        elif choi == '4':
                            update_supplier_detalis()
                        elif choi =='5':
                            update_inventory_detalis()
                        elif choi=='6':
                            update_employee_detalis()    
                        elif choi =='7':
                            break
                        else:
                            print("Invalid choice. Please try again.")            
                elif ch == '3':
                    while True:
                        print("which table would you like delete the detalis from?")    
                        print("1.Product Table")
                        print("2.Customer Table")
                        print("3.Sales Table")
                        print("4.Suppiler Table")
                        print("5.Inventory Table")
                        print("6.Employee Table ")
                        print("7.Exit")
                        choi=(input("Enter your choice:"))
                        if choi==1:
                            delete_product_detalis() 
                        elif choi == '2':
                            delete_customer_detalis()
                        elif choi == '3':
                            delete_sales_detalis()
                        elif choi == '4':
                            delete_supplier_detalis()
                        elif choi =='5':
                            delete_inventory_detalis()
                        elif choi=='6':
                            delete_employee_detalis()    
                        elif choi =='7':
                            break
                        else:
                            print("Invalid choice. Please try again.")            
                if ch == '4':
                    while True:
                            print("which table would you like display the detalis?")    
                            print("1.Product Table")
                            print("2.Customer Table")
                            print("3.Sales Table")
                            print("4.Suppiler Table")
                            print("5.Inventory Table")
                            print("6.Employee Table ")
                            print("7.Exit")
                            choi=(input("Enter your choice:"))
                            if choi==1:
                                display_product_detalis() 
                            elif choi == '2':
                                display_customer_detalis()
                            elif choi == '3':
                                display_sales_detalis()
                            elif choi == '4':
                                display_supplier_detalis()
                            elif choi =='5':
                                display_inventory_detalis()
                            elif choi=='6':
                                display_employee_detalis()    
                            elif choi =='7':
                                break
                            else:
                                print("Invalid choice. Please try again.")
                elif ch == '5':
                    while True:
                        print("which table would you like search ?")    
                        print("1.Product Table")
                        print("2.Customer Table")
                        print("3.Sales Table")
                        print("4.Suppiler Table")
                        print("5.Inventory Table")
                        print("6.Employee Table ")
                        print("7.Exit")
                        choi=(input("Enter your choice:"))
                        if choi==1:
                            search_product_detalis() 
                        elif choi == '2':
                            search_customer_detalis()
                        elif choi == '3':
                            search_sales_detalis()
                        elif choi == '4':
                            search_supplier_detalis()
                        elif choi =='5':
                            search_inventory_detalis()
                        elif choi=='6':
                            search_employee_detalis()    
                        elif choi =='7':
                            break
                        else:
                            print("Invalid choice. Please try again.")            
                elif ch == '6':
                    break                
        else:
            print("Invalid admin credentials. Please try again.")
        
    elif choice == '2':
       print("Thank you for visiting mobileshop database!")
       break

    else:
        print("Invalid choice. Please try again.")
   