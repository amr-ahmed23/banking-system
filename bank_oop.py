class Account:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.\n")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful.\n")
        else:
            print("Not enough balance.\n")

    def display(self):
        print(f"Account: {self.number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}\n")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        number = input("Enter new account number: ")
        if number in self.accounts:
            print("This account already exists.")
            return
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial deposit: "))
        self.accounts[number] = Account(number, name, balance)
        print("Account created successfully.\n")

    def deposit(self):
        number = input("Enter account number: ")
        account = self.accounts.get(number)
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("Account not found.\n")

    def withdraw(self):
        number = input("Enter account number: ")
        account = self.accounts.get(number)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("Account not found.\n")

    def check_balance(self):
        number = input("Enter account number: ")
        account = self.accounts.get(number)
        if account:
            account.display()
        else:
            print("Account not found.\n")

    def run(self):
        while True:
            print("=== Simple Banking System (OOP) ===")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid option.\n")

bank = Bank()
bank.run()
