# Banking System - Procedural Approach

# We use a dictionary to store account data
accounts = {}

def create_account():
    acc_number = input("Enter new account number: ")
    if acc_number in accounts:
        print("This account already exists.")
        return
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit: "))
    accounts[acc_number] = {"name": name, "balance": balance}
    print("Account created successfully.\n")

def deposit():
    acc_number = input("Enter account number: ")
    if acc_number not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter deposit amount: "))
    accounts[acc_number]["balance"] += amount
    print("Deposit successful.\n")

def withdraw():
    acc_number = input("Enter account number: ")
    if acc_number not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter withdrawal amount: "))
    if accounts[acc_number]["balance"] >= amount:
        accounts[acc_number]["balance"] -= amount
        print("Withdrawal successful.\n")
    else:
        print("Not enough balance.\n")

def check_balance():
    acc_number = input("Enter account number: ")
    if acc_number in accounts:
        acc = accounts[acc_number]
        print(f"Account: {acc_number}")
        print(f"Name: {acc['name']}")
        print(f"Balance: {acc['balance']}\n")
    else:
        print("Account not found.\n")

def main():
    while True:
        print("=== Simple Banking System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid option. Try again.\n")

# Start the program
main()
