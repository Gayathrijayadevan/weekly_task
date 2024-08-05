import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table customers(customer_id text,customer_name text ,email text,phone int,address text,age int)")
except:
    pass   
def add_customer_details():
        a=int(input("Enter no. of customers: "))
        for i in range(a):
            id=input("Enter customer id:")
            name=str(input("Enter customer name:"))
            email=input("Enter email:")
            phone=int(input("Enter phone number:"))
            address=input("Enter address:")
            age=int(input("Enter age:"))

            con.execute("insert into customers(customer_id,customer_name,email,phone,address,age) values(?,?,?,?,?,?)",(id,name,email,phone,address,age))
            con.commit()

def update_customer_detalis():
        a = input("Enter name to update:")
        b = input("Enter new name:")
        c=input("Enter email:")
        d=int(input("Enter phone number:"))
        e=input("Enter address:")
        f=int(input("Enter age:"))
        
        con.execute(
    "UPDATE customers SET customer_name=?, email=?, phone=?, address=?, age=? WHERE customer_name=?",(b, c, d, e, f, a,))

        
def delete_customer_detalis():
        a=input("Enter customer  id to delete:")
        con.execute("DELETE from customers WHERE customer_id=?",(a,))
        con.commit()

def display_customer_detalis():
        data=con.execute("select * from customers")  
        print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format("customer id","customer name", "email", "phone","address","age"))
        print('_' * 80)
        for i in data:
            print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def search_customer_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from customers where customer_id=?",(a,))
        print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format("customer id","customer name", "email", "phone","address","age"))
        print('_' * 80)
        for i in data:
                f=1
                print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format(i[0], i[1], i[2],i[3],i[4],i[5]))
        if f==0:
            print("sorry this person is not in the table")
def orderby_customer():
        data=con.execute("select *from customers order by customer_id")
        print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format("customer id","customer name", "email", "phone","address","age"))
        print('_' * 80)
        for i in data:
            print("{:<15}{:<15}{:<20}{:<10}{:<10}{:<6}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def groupby_customer():
    data=con.execute("select customer_name from customers group by age ")
    for i in data:
            print(i)