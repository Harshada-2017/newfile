class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Money deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Money withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("Current Balance:", self.balance)


b = Bank()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        b.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        b.withdraw(amount)

    elif choice == 3:
        b.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")