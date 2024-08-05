import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table products(product_id text,product_name text ,brand text,model text,speci text,price int ,stock int,suppiler_id text)")
except:
    pass   
def add_product_details():
        a=int(input("Enter no. of products: "))
        for i in range(a):
            id=input("Enter id:")
            name=str(input("Enter product name:"))
            brand=str(input("Enter brand name:"))
            model=input("Enter model:")
            specifi=input("Enter specification:")
            price=int(input("Enter product price:"))
            stock=int(input("Enter the stock:"))
            supply=input("Enter the supplier id:")
            con.execute("insert into products(product_id,product_name,brand,model,speci,price,stock,suppiler_id) values(?,?,?,?,?,?,?,?)",(id,name,brand,model,specifi,price,stock,supply))
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
        con.execute("UPDATE products SET product_name=?,brand=?,model=?,speci=?,price=?,stock=?,suppiler_id=? WHERE product_name=?", (b,c,d,e,f,g,h,a,))
        con.commit()

def delete_product_detalis():
        a=input("Enter product id to delete:")
        con.execute("DELETE from products WHERE product_id=?",(a,))
        con.commit()

def display_product_detalis():
        data=con.execute("select * from products")  
        print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format("product_id","product_name", "brand_name", "model","specification","price","stock","supplier_id"))
        print('_' * 100)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7]))

def search_product_detalis():
        a=input("Enter the  product id you want to search:") 
        f=0       
        data=con.execute("select * from products where product_id=?",(a,))
        print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format("product_id","product_name", "brand_name", "model","specification","price","stock","supplier_id"))
        print('_' * 100)
        for i in data:
            f=1
            print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7]))
        if f==0:
            print("sorry this product is not in the table")

def orderby_product():
        data=con.execute("select *from products order by product_id ")
        print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format("product_id","product_name", "brand_name", "model","specification","price","stock","supplier_id"))
        print('_' * 100)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<10}{:<15}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7]))

def groupby_product():
    data=con.execute("select product_name from products group by  price ")
    for i in data:
            print(i)