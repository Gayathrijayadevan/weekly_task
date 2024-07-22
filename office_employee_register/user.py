from datetime import datetime
users = {}
admin={'username':'admin' ,'password': '123'}
current_user = None
activity_logs = []

def log_activity(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    activity_logs.append(f"{timestamp} - {activity}")


def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    log_activity(f"User registered: {username}")
    return True

def login_user(username, password):
    global current_user
    if username in users and users[username] == password:
        current_user = {"username": username}
        log_activity(f"User logged in: {username}")
        return True
    return False

def logout_user(username):
    global current_user
    current_user = None
    log_activity(f"User logged out: {username}")
    print("Logged out successfully.")

def is_admin1(username,password):
    for i in admin:
        print(i,admin[i])
    if username== 'admin' and  password=='123':
        return True
    log_activity(f"Admin logged in: {username}")
    return False

def view_activity_logs():
    print("\nActivity Logs:")
    for log in activity_logs:
        print(log)

def search_employee(dtl, s):
    results = []
    search = s.lower()
    for i in dtl:
        if search in i['name'].lower() :
            for i in results:
                print(i)
            results.append(i)
    return results     