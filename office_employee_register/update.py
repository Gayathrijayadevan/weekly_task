def update_detalis(dtl):
    avli_name=input("Enter the name of employee :")
    f=0
    for i in dtl:
        if i['name']==avli_name:
            new_name=input("Enter new name:")
            i.update("name":new_name)

            new_age=int(input("Enter new age:"))
            i.update("age":new_age)

            new_dept=input("Enter new department name:")
            i.update("dept":new_dept)

            new_place=input("Enter new place:" )
            i.update("place":new_place)

            new_number=int(input("Enter new phone number:"))
            i.update("number":new_number)
            f=1
        if f==0:
            print("sorry this name is not present in the register")    
            
