
def add_detalis(dtl):
        name=input("Enter name:")
        age=int(input("Enter age:"))
        job=input("Enter job:")
        department=input("Enter department")
        place=input("Enter course:")
        number=int(input("Enter phone number:"))
        dtl.append({'name':name,'age':age,'job':job,'dept':department,'place':place
                    ,'num':number}) 
