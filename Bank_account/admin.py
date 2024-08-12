import os
from account_activities import *

def admin_view_all_users(directory_path):
    if not os.path.exists(directory_path):
        print("No accounts found!")
        return

    files = os.listdir(directory_path)
    if not files:
        print("No accounts found!")
    else:
        print("List of all users:")
        for file_name in files:
            account_file_path = os.path.join(directory_path, file_name)
            account_number, username, password, balance = read_account(account_file_path)
            print(f"Account Number: {account_number}, Username: {username}, Balance: ${balance:.2f}")
