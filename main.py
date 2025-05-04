class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} is deposited successfully. Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} was withdrawed succesfully. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
        
    def transfer(self, other_account, amount):
        if amount <= self.balance:
            if isinstance(other_account, BankAccount):
                self.balance -= amount
                other_account.balance += amount
                print(f"you have transfered ${amount} successfully to {other_account.owner}, Your balance: ${self.balance}")
            else:
                print("This user does not exist")
        else:
            print("Insufficient funds.")
        
my_account = BankAccount("Daler")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.show_balance()
            
other_account = BankAccount("Baxa")
my_account.transfer(other_account, 200)
other_account.show_balance()