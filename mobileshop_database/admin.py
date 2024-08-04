admin={'username':'admin' ,'password': '123'}


def is_admin1(username,password):
    for i in admin:
        print(i,admin[i])
    if username== 'admin' and  password=='123':
        return True
    return False