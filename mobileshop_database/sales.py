import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table sales(sale_id text,product_id text ,customer_id text,date text,price int ,payment_method text)")
except:
    pass   
def add_sales_details():
        a=int(input("Enter no. of sales: "))
        for i in range(a):
            sales_id=input("Enter sales id:")
            prod_id=input("Enter product id:")
            cust_id=input("Enter customer id:")
            date=input("Enter date of purchase:")
            price=int(input("Enter price:"))
            method=input("Enter payment method:")

            con.execute("insert into sales(sale_id,product_id,customer_id,date,price,payment_method) values(?,?,?,?,?,?)",(sales_id,prod_id,cust_id,date,price,method))
            con.commit()

def update_sales_detalis():
        a =input("Enter sales id to update:")
        b = input("Enter new id:")
        c=input("Enter product id")
        d=input("Enter customer id:")
        e=input("Enter date:")
        f=int(input("Enter new price:"))
        g=input("Enter payment method:")
        
        con.execute("UPDATE sales SET sale_id=?,product_id=?,customer_id=?,date=?,price=?,payment_method=? WHERE sale_id=?", (b,c,d,e,f,g,a,))
        con.commit()
            
def delete_sales_detalis():
        a=input("Enter sale id to delete:")
        con.execute("DELETE from sales WHERE sale_id=?",(a,))
        con.commit()

def display_sales_detalis():
        data=con.execute("select * from sales")  
        print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format("sale id","product id", "customer id", "date","price","payment method"))
        print('_' * 80)
        for i in data:
            print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def search_sales_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from sales where sale_id=?",(a,))
        print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format("sales id","product id", "customer id", "date","price","payment method"))
        print('_' * 80)
        for i in data:
                f=1
                print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))
        if f==0:
            print("sorry this person is not in the table")
def orderby_sales():
      data=con.execute("select *from sales order by sale_id")
      print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format("sale id","product id", "customer id", "date","price","payment method"))
      print('_' * 80)
      for i in data:
            print("{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def groupby_sales():
        data=con.execute("select product_id from sales group by product_id ")
        for i in data:
            print(i)
