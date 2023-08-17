from tabulate import tabulate
import random
import datetime

users = []
transactions = [] 
account_number_counter = 123450000001
trans_counter = 10000000000000000000

def transaction():
    global trans_counter
    trans_counter += 1
    return trans_counter

def reg_user():
    global account_number_counter
    global trans_counter
    full_name = input("Enter your full name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    account_number = account_number_counter
    account_number_counter += 1
    users.append([full_name, account_number, initial_deposit])
    transactions.append([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                transaction(),
                "CR",
                initial_deposit,
                users[0][2],
                'OK'])
reg_user()
    

while True:
    print("\nSelect type:\n1 -> Debit\n2 -> Credit\n3 -> Print statement\n4 -> Check Balance\n5 -> Exit\n")
    choice = input("Enter your choice: ")
    
    if choice == "1":  # Debit
        amount = float(input("Enter debit amount: "))
        if amount <= users[0][2]:
            users[0][2] -= amount
            transactions.append([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                transaction(),
                "DE",
                amount,
                users[0][2],
                'OK'
            ])
            print("Balance left: " , users[0][2])
        else:
            print("Insufficient balance for debit.")
    
    elif choice == "2":  # Credit
        amount = float(input("Enter credit amount: "))
        users[0][2] += amount
        transactions.append([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            transaction(),
            "CR",
            amount,
            users[0][2],
            'OK'
        ])
    
    elif choice == "3":  # Print statement
        str1 = str(users[0][1])[-4:]
        print("WELCOME TO OUR LOCAL BANK".center(100, '*'))
        print("Account holder name: ", users[0][0], "\nAccount Number: ", str1.rjust(12, '*'), "\nBank Name: Local Bank Of Varun Kumar")
        print(tabulate(list(transactions), headers=["Date", "Transaction ID", "Transaction Type", "Amount", "Balance", "Remarks"], tablefmt="pretty"))
        print("Statement Printed Successfully!!".center(100, '*'))
    
    elif choice == "4":  # Check balance
        print("Available balance:", users[0][2])
    
    elif choice == "5": #exit
        break
    
    else:
        print("Invalid choice. Please select a valid transaction type.")
