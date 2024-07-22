def update_details(dtl):
    avli_name = input("Enter the name of employee: ")
    f = 0
    for i in dtl:
        if i['name'] == avli_name:
            new_name = input("Enter new name (leave blank to keep current name): ")
            if new_name:
                i.update({"name": new_name})

            new_age = input("Enter new age (leave blank to keep current age): ")
            if new_age:
                i.update({"age": new_age})

            new_job = input("Enter new job (leave blank to keep current job ): ")
            if new_job:
                    i.update({"job": new_job})
            
            new_dept = input("Enter new department (leave blank to keep current department): ")
            if new_dept:
                    i.update({"dept": new_dept})

            new_place = input("Enter new place (leave blank to keep current place): ")
            if new_place:
                    i.update({"place": new_place})

            new_num = input("Enter new  phone number (leave blank to keep current  number): ")
            if new_num:
                    i.update({"place": new_num})

            f = 1
            print("Details updated successfully.")
            break
    
    if f == 0:
        print("Sorry, this name is not present in the register.")
