import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table sales(sale_id int,product_id int ,customer_id,date int,price int ,payment_method text)")
except:
    pass   
def add_sales_details():
        a=int(input("Enter no. of sales: "))
        for i in range(a):
            sales_id=int(input("Enter sales id:"))
            prod_id=int(input("Enter product id:"))
            cust_id=int(input("Enter customer id:"))
            date=int(input("Enter date of purchase:"))
            method=input("Enter payment method:")

            con.execute("insert into sales(sale_id,product_id,customer_id,date,price,payment_method) values(?,?,?,?,?,?)",(sales_id,prod_id,cust_id,date,method))
            con.commit()

def update_sales_detalis():
        a =int( input("Enter sales id to update:"))
        b =int( input("Enter new id:"))
        c=int(input("Enter product id"))
        d=int(input("Enter customer id:"))
        e=int(input("Enter date:"))
        f=input("Enter payment method:")
        
        con.execute("UPDATE sales SET sale_id=?,product_id=?,customer_id=?,date=?,price=?,payment_method=? WHERE sale_id=?", (b,c,d,e,f,a,))
        con.commit()
            
def delete_sales_detalis():
        a=input("Enter sale id to delete:")
        con.execute("DELETE from sales WHERE sale_id=?",(a,))
        con.commit()

def display_sales_detalis():
        data=con.execute("select * from staff")  
        print("{:<6}{:<6}{:<6}{:<6}{:<6}{:<10}".format("sale id","product id", "customer id", "date","price","payment method"))
        print('_' * 60)
        for i in data:
            print("{:<6}{:<6}{:<6}{:<6}{:<6}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def search_sales_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from staff where id=?",(a,))
        print("{:<6}{:<6}{:<6}{:<6}{:<6}{:<10}".format("sale id","product id", "customer id", "date","price","payment method"))
        print('_' * 60)
        for i in data:
                f=1
                print("{:<6}{:<6}{:<6}{:<6}{:<6}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))
        if f==0:
            print("sorry this person is not in the table")
    