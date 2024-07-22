
def add_detalis(dtl):
        id=int(input("Enter id:"))
        name=input("Enter name:")
        age=int(input("Enter age:"))
        job=input("Enter job:")
        department=input("Enter department:")
        place=input("Enter place:")
        number=int(input("Enter phone number:"))
        dtl.append({'id': id,'name':name,'age':age,'job':job,'dept':department,'place':place
                    ,'num':number}) 
