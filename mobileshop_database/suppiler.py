import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table supplier(suppiler_id text PRIMARY KEY,suppiler_name text ,phone int,email text,address text)")
except:
    pass   
def add_supplier_details():
        a=int(input("Enter no. of suppiler: "))
        for i in range(a):
            id=input("Enter suppiler id:")
            name=str(input("Enter suppiler  name:"))
            phone=int(input("Enter phone number:"))
            email=input("Enter email:")
            address=input("Enter address:")

            con.execute("INSERT INTO supplier(suppiler_id,suppiler_name,phone,email,address) values(?,?,?,?,?)",(id,name,phone,email,address))
            con.commit()

def update_supplier_detalis():
        a = input("Enter name to update:")
        b = input("Enter new name:")
        c=int(input("Enter phone number:"))
        d=input("Ënter email:")
        e=input("Enter address:")
        
        con.execute("UPDATE supplier SET suppiler_name=?,phone=?,email=?,address=? WHERE name=?", (b,c,d,e,a))
        con.commit()

def delete_supplier_detalis():
        a=input("Enter suppiler id to delete:")
        con.execute("DELETE from supplier WHERE suppiler_id=?",(a,))
        con.commit()

def display_supplier_detalis():
        data=con.execute("select * from supplier")  
        print("{:<15}{:<15}{:<15}{:<20}{:<20}".format("suppiler_id","suppiler_name", "phone number", "email","address"))
        print('_' * 70)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<20}{:<20}".format(i[0], i[1], i[2],i[3],i[4]))

def search_supplier_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from supplier where suppiler_id=?",(a,))
        print("{:<15}{:<15}{:<15}{:<20}{:<20}".format("suppiler_id","suppiler_name", "phone number", "email","address"))
        print('_' * 70)
        for i in data:
                f=1
                print("{:<15}{:<15}{:<15}{:<20}{:<20}".format(i[0], i[1], i[2],i[3],i[4]))

        if f==0:
            print("sorry this person is not in the table")

def orderby_supplier():
      data=con.execute("select *from supplier  order by suppiler_id")
      print("{:<15}{:<15}{:<15}{:<20}{:<20}".format("suppiler_id","suppiler_name", "phone number", "email","address"))
      print('_' * 70)
      for i in data:
            print("{:<15}{:<15}{:<15}{:<20}{:<20}".format(i[0], i[1], i[2],i[3],i[4]))

def groupby_suppiler():
        data=con.execute("select suppiler_name from supplier group by suppiler_name ")
        for i in data:
            print(i)
