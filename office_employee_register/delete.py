def remove(dtl):
    a_name=input("Enter the name of employee:")
    for i in dtl:
        if i["name"]==a_name:
            dtl.remove(i)