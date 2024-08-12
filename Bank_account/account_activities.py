import os
import random

def generate_unique_account_number(directory_path):
    while True:
        account_number = random.randint(1000000000, 9999999999)  
        account_file_path = os.path.join(directory_path, f"{account_number}.txt")
        
        if not os.path.exists(account_file_path):
            return account_number

def create_account(directory_path):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    acc_no = generate_unique_account_number(directory_path)
    account_file_path = os.path.join(directory_path, f"{acc_no}.txt")

    with open(account_file_path, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Balance: 0.0\n")

    print(f"Account created successfully! Your account number is {acc_no}.")

def read_account(account_file_path):
    with open(account_file_path, "r") as file:
        data = file.readlines()
        username = data[0].strip().split(": ")[1]
        password = data[1].strip().split(": ")[1]
        balance = float(data[2].strip().split(": ")[1])
    account_number = os.path.basename(account_file_path).replace(".txt", "")
    
    return account_number, username, password, balance



def update_balance(account_file_path, new_balance):
    username, password, _ = read_account(account_file_path)
    with open(account_file_path, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Balance: {new_balance}\n")


def deposit(directory_path,user,account_number, amount):
    account_file_path = os.path.join(directory_path, f"{account_number}.txt")
    if not os.path.exists(account_file_path):
        print("Account not found!")
        return
    username, password, balance = read_account(account_file_path)
    new_balance = balance + amount
    update_balance(account_file_path, new_balance)
    print(f"Successfully deposited ${amount}. New balance: ${new_balance:.2f}")

def withdraw(directory_path,user,account_number, amount):
    account_file_path = os.path.join(directory_path, f"{account_number}.txt")
    if not os.path.exists(account_file_path):
        print("Account not found!")
        return

    username, password, balance = read_account(account_file_path)
    if amount > balance:
        print("Insufficient funds!")
        return

    new_balance = balance - amount
    update_balance(account_file_path, new_balance)
    print(f"Successfully withdrew ${amount}. New balance: ${new_balance:.2f}")


def display_accounts(directory_path):
    if not os.path.exists(directory_path):
        print("No accounts found!")
        return

    files = os.listdir(directory_path)
    if not files:
        print("No accounts found!")
    else:
        print("List of accounts:")
        for file_name in files:
            account_file_path = os.path.join(directory_path, file_name)
            account_number, username, password, balance = read_account(account_file_path)
            print(f"Account Number: {account_number}, Username: {username}, Balance: ${balance:.2f}")
