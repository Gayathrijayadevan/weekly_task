import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table products(product_id int,product_name text ,brand text,model text,speci text,price int ,stock int,suppiler_id int)")
except:
    pass   
def add_product_details():
        a=int(input("Enter no. of employees: "))
        for i in range(a):
            id=int(input("Enter id:"))
            name=str(input("Enter product name:"))
            brand=str(input("Enter brand name:"))
            model=input("Enter model:")
            specifi=input("Enter specification:")
            price=int(input("Enter product price:"))
            stock=int(input("Enter the stock:"))
            supply=int(input("Enter the supplier:"))
            con.execute("insert into product(product_id,product_name,brand,model,speci,price,stock,suppiler_id) values(?,?,?,?,?,?,?,?)",(id,name,brand,model,specifi,price,stock,supply))
            con.commit()

def update_product_detalis():
        a = input("Enter name to update:")
        b = input("Enter new name:")
        c=input("Enter brand name:")
        d=input("Enter model:")
        e=input("Enter specification:")
        f=input("Enter price:")
        g=input("Enter stock:")
        h=input("Enter suppiler id:")
        con.execute("UPDATE staff SET name=?,brand=?,model=?,specifi=?,price=?,stock=?,supply=? WHERE product_name=?", (b,c,d,e,f,g,h,a,))
        con.commit()

def delete_product_detalis():
        a=input("Enter product id to delete:")
        con.execute("DELETE from products WHERE product_id=?",(a,))
        con.commit()

def display_product_detalis():
        data=con.execute("select * from products")  
        print("{:<6}{:<10}{:<10}{:<6}{:<15}{:<6}{:<6}{:<6}".format("product_id","product_name", "brand_name", "model","specification","price","stock","supplier_id"))
        print('_' * 80)
        for i in data:
            print("{:<6}{:<10}{:<10}{:<6}{:<15}{:<6}{:<6}{:<6}".format(i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7]))

def search_product_detalis():
        a=input("Enter the  product id you want to search:") 
        f=0       
        data=con.execute("select * from products where product_id=?",(a,))
        print("{:<6}{:<10}{:<10}{:<6}{:<15}{:<6}{:<6}{:<6}".format("product_id","product_name", "brand_name", "model","specification","price","stock","supplier_id"))
        print('_' * 80)
        for i in data:
            f=1
            print("{:<6}{:<10}{:<10}{:<6}{:<15}{:<6}{:<6}{:<6}".format(i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7]))
        if f==0:
            print("sorry this product is not in the table")
    