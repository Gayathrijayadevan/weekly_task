import sqlite3

con=sqlite3.connect("database/sqlte3/prog1.db")
try:
    con.execute("create table products(product_id int,product_name text ,brand text,model text,speci text,price int ,stock int,suppiler_id int)")
except:
    pass   
def add_employee_details():
        a=int(input("Enter no. of employees: "))
        for i in range(a):
            id=int(input("Enter id:"))
            name=str(input("Enter name:"))
            age=int(input("Enter age:"))
            email=input("Enter email:")
            salary=int(input("Enter salary:"))

            con.execute("insert into staff(id,name,age,email,salary) values(?,?,?,?,?)",(id,name,age,email,salary))
            con.commit()

def update_employee_detalis():
        a = input("Enter name to update:")
        b = input("Enter new name:")
        data=con.execute("select * from staff where name=?",(a,))
        for i in data:
            f=1
            con.execute("UPDATE staff SET name=? WHERE name=?", (b, a))
            con.commit()

        if f==0:
            print("sorry this name is not in the list:")
            
def delete_employee_detalis():
        a=input("Enter id to delete:")
        con.execute("DELETE from staff WHERE id=?",(a,))
        con.commit()

def display_employee_detalis():
        data=con.execute("select * from staff")  
        print("{:<6}{:<10}{:<6}{:<15}{:<10}".format("id","name", "age", "email","salary"))
        print('_' * 50)
        for i in data:
            print("{:<6}{:<10}{:<6}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4]))

def search_employee_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from staff where id=?",(a,))
        print("{:<6}{:<10}{:<6}{:<15}{:<10}".format("id","name", "age", "email","salary"))
        print('_' * 50)
        for i in data:
                f=1
                print("{:<6}{:<10}{:<6}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4]))
        if f==0:
            print("sorry this person is not in the table")
    