import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table inventory(inventory_id text,product_id text,stock_recived int ,date text,stock_sold int,date_sold text )")
except:
    pass   
def add_inventory_details():
        a=int(input("Enter no. of inventory: "))
        for i in range(a):
            id=input("Enter inventory id:")
            p_id=input("Enter product id:")
            stock_re=int(input("Enter stock recived:"))
            date_stock=input("Enter date of stock received:")
            stock_sold=int(input("Enter stock sold:"))
            date_sold=input("Enter date sold")

            con.execute("insert into inventory(inventory_id,product_id,stock_recived,date,stock_sold,date_sold) values(?,?,?,?,?,?)",(id,p_id,stock_re,date_stock,stock_sold,date_sold))
            con.commit()

def update_inventory_detalis():
        a = input("Enter inventory id  to update:")
        b =input("Enter new id:")
        c= input("Enter product id:")
        d=int(input("Enter new stock received:"))
        e=input("Enter date it received:")
        f=int(input("Enter new stocksold:"))
        g=input("Enter new date received:")
        
        con.execute("UPDATE inventory SET inventory_id=?,product_id=?,stock_recived=?,date=?,stock_sold=?,date_sold=? WHERE inventory_id=?", (b,c,d,e,f,g, a))
        con.commit()

def delete_inventory_detalis():
        a=input("Enter inventory id to delete:")
        con.execute("DELETE from inventory WHERE inventory_id=?",(a,))
        con.commit()

def display_inventory_detalis():
        data=con.execute("select * from inventory")  
        print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format("inventory_id","product_id","stock_recived","date","stock_sold","date_sold"))
        print('_' * 80)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def search_inventory_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from inventory where inventory_id=?",(a,))
        print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format("inventory_id","product_id","stock_recived","date","stock_sold","date_sold"))
        print('_' * 80)
        for i in data:
                f=1
                print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

        if f==0:
            print("sorry this product is not in the table")

def orderby_inventory():
        data=con.execute("select * from inventory order by inventory_id")
        print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format("inventory_id","product_id","stock_recived","date","stock_sold","date_sold"))
        print('_' * 80)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<16}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def groupby_inventory():
      data=con.execute("select stock_recived  from inventory group by product_id ")
      for i in data:
            print(i)

