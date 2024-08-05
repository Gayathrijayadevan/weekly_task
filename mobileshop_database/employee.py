import sqlite3

con=sqlite3.connect("weekly_task/mobileshop_database/weeklytask.db")
try:
    con.execute("create table employees(emp_id text,emp_name text ,pos text,email text,phone int ,date_hire text)")
except:
    pass   
def add_employee_details():
        a=int(input("Enter no. of employees: "))
        for i in range(a):
            id=input("Enter id:")
            name=str(input("Enter name:"))
            posi=input("Enter position:")
            email=input("Enter email:")
            phone=int(input("Enter phone number:"))
            date_h=input("Enter date hired")

            con.execute("insert into employees(emp_id,emp_name ,pos,email,phone ,date_hire) values(?,?,?,?,?,?)",(id,name,posi,email,phone,date_h))
            con.commit()

def update_employee_detalis():
        f=0
        a = input("Enter  employee name to update:")
        b = input("Enter new name:")
        c=input("Enter new position:")
        d=input("Ënter email:")
        e=int(input("Enter  new phone number:"))
        f=input("Enter date heird:")
        con.execute("UPDATE employees SET emp_name=?,pos=?,email=?,phone=?,date_hire=? WHERE emp_name=?", (b,c,d,e,f,a))
        f=1
        con.commit()

        if f==0:
            print("sorry this name is not in the list:")
            
def delete_employee_detalis():
        a=input("Enter id to delete:")
        con.execute("DELETE from employees WHERE emp_id=?",(a,))
        con.commit()

def display_employee_detalis():
        data=con.execute("select * from employees")  
        print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format("employee_id","employee_name" ,"position","email","phone number" ,"date_hired"))
        print('_' * 70)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def search_employee_detalis():
        a=input("Enter the id you want to search:") 
        f=0       
        data=con.execute("select * from employees where emp_id=?",(a,))
        print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format("employee_id","employee_name" ,"position","email","phone number" ,"date_hired"))
        print('_' * 70)
        for i in data:
                f=1
                print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))
        if f==0:
            print("sorry this person is not in the table")
def orderby_employee():
        data=con.execute("select *from employees order by emp_id")
        print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format("employee_id","employee_name" ,"position","email","phone number" ,"date_hired"))
        print('_' * 70)
        for i in data:
            print("{:<15}{:<15}{:<15}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

def groupby_employee():
    data=con.execute("select emp_name from employees group by pos ")
    for i in data:
            print(i)
  