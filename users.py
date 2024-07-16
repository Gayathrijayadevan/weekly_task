users = {}
admin={'username':'admin' ,'password': '123'}
current_user = None

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True

def login_user(username, password):
    global current_user
    if username in users and users[username] == password:
        current_user = {"username": username}
        print(current_user)
        return True
    return False

def logout_user():
    global current_user
    current_user = None

def is_admin(username, password):
    if username== admin['username'] and admin['password'] == password:
        return True
    return False