# atm_system.py

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"

    def authenticate(self):
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == self.pin:
            print("Authentication successful.")
            return True
        else:
            print("Incorrect PIN.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def start(self):
        if not self.authenticate():
            return
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    atm = ATM(balance=1000)
    atm.start()
