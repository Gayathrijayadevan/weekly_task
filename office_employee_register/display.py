def display_details(dtl):
    print("{:<6}{:<15}{:<6}{:<10}{:<12}{:<10}{:<15}".format("id","name", "age", "job", "department", "place", "number"))
    print('_' * 68)
    for i in dtl:
        print("{:<6}{:<15}{:<6}{:<10}{:<12}{:<10}{:<15}".format(i['id'],i['name'], i['age'], i['job'], i['dept'], 
                                                           i['place'], i['num']))

def admin_view(dtl):
    print("{:<6}{:<15}{:<6}{:<10}{:<12}{:<10}{:<15}".format("id","name", "age", "job", "department", "place", "number"))
    print('_' * 68)
    for i in dtl:
        print("{:<6}{:<15}{:<6}{:<10}{:<12}{:<10}{:<15}".format(i['id'],i['name'], i['age'], i['job'], i['dept'],
                                                            i['place'], i['num']))

