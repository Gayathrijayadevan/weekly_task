def display_detalis(dtl):
    print("{:<10}{:<6}".format("name","age","job","department","place","number"))
    print('_'*20)
    for i in dtl:
        print(("{:<10}{:<6}").formate(i['name'],i['age'],i['job'],i['department'],i['place'],i['number']))
