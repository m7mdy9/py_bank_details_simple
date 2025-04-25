import random
import time

bank_names = ["Bank Misr", "Alahly Bank", "CIB Bank", "The Argricultural Bank"]
chosen_bank = random.choice(bank_names)

def sleep(n):
    time.sleep(n)

accounts = {
    "1": {
        "ID": 1,
        "name": "mohamed elenany",
        "email": "mohamed@gmail.com",
        "balance": 0
    },
    "2": {
        "ID": 2,
        "name": "farah khaled",
        "email": "farah@gmail.com",
        "balance": 100
    },
    "3": {
        "ID": 3,
        "name": "zeina ayman",
        "email": "zeina@gmail.com",
        "balance": 300
    },
    "4": {
        "ID": 4,
        "name": "joudy seif",
        "email": "joudy@gmail.com",
        "balance": 400
    }
}

def welcome():
    print(f"Welcome to {chosen_bank}")

def account_verification():
    print(f"Enter your account ID")
    sleep(0.5)
    looper = True
    while looper:
        id = input(">")
        if id not in list(accounts.keys()):
            print("Invalid account ID.")
            sleep(0.5)
        else:
            looper = False
    return id

def details(id):
    print(accounts.get(id))
    sleep(0.5)

def deposit(id):
    id = str(id)
    looper = True
    while looper:
        amount = input("Enter amount to deposit: ")
        sleep(0.5)
        if amount.isdigit() and int(amount) > 0:
            looper = False
        else:
            print("Please enter a positive number.")
            sleep(0.5)
    account = accounts.get(id)
    account["balance"] = account.get("balance") + int(amount)
    
    # accounts.update({ str(id):{"balance": balance+amount}})
    print(f"Deposited {amount}, Current Balance is {account["balance"]}")
    sleep(0.5)

def withdraw(id):
    id = str(id)
    account = accounts.get(id)
    looper = True
    while looper:
        amount = input("Enter amount to withdraw: ")
        sleep(0.5)
        if amount.isdigit():
            if int(amount) <= account.get("balance") and int(amount) > 0:
                looper = False
            else:
                print(f"Please enter a positive number and make sure it doesn't exceed your balance. ({account.get("balance")})")
                sleep(0.5)
        else:
            print(f"Please enter a positive number and make sure it doesn't exceed your balance. ({account.get("balance")})")
            sleep(0.5)
    account["balance"] = account["balance"] - int(amount)
    
    # accounts.update({ str(id):{"balance": balance+amount}})
    print(f"Withdrawn {amount}, Current Balance is {account["balance"]}")
    sleep(0.5)