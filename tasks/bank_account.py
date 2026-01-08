class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}$ is added to the account")
        else:
            print("Invalid deposit amount")

    def Withdrawal(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount}$ withdrawn from the account")
            else:
                print("Insufficient balance")
        else:
            print(f"Invalid withdrawal amount")

    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Bank fee if {fee}$ applied  ")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance}$")


newAccount = BankAccount(2178514584, "Maria", 2700)
newAccount.Withdrawal(300)
newAccount.Deposite(200)
newAccount.display()
