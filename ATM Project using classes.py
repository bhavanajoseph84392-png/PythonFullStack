class ATM:

    def __init__(self):
        self.name = "Bhavana"
        self.mobile_number = ""
        self.atm_pin = "4400"
        self.balance = 98567
        self.transaction_history = []

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))

        if amount <= 1000 and amount % 100 != 0:
            print("Minimum deposit should be above 1000")
            print("Enter amount in multiples of 100")

        else:
            self.balance += amount
            self.transaction_history.append(f"Deposit: {amount}")
            print(f"{amount} deposited successfully")

    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn: "))

        if amount > self.balance and  amount % 100 != 0:
            print("Insufficient balance")
            print("Enter amount in multiples of 100")

        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: {amount}")
            print(f"Withdrawal successful! New balance: {self.balance}")

    def change_pin(self):
        new_pin = input("Enter your new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            self.atm_pin = new_pin
            print("PIN changed successfully.")

        else:
            print("Invalid PIN. Please enter exactly 4 digits.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def mini_statement(self):
        print("\nTransaction History")

        if not self.transaction_history:
            print("No transactions yet.")

        else:
            for record in self.transaction_history:
                print(record)

    def verify_pin(self):
        attempts = 3

        while attempts > 0:

            pin = input("Enter your ATM PIN: ")

            if pin == self.atm_pin:
                return True

            attempts -= 1

            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempt(s) remaining.")

        print("Card blocked temporarily due to too many failed attempts.")
        return False

    def atm_menu(self):

        while True:

            print(" ATM MENU ")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Change PIN")
            print("4. Check Balance")
            print("5. Mini Statement")
            print("6. Exit")

            selection = input("Enter your selection: ")

            if selection == "1":
                self.deposit()

            elif selection == "2":
                self.withdraw()

            elif selection == "3":
                self.change_pin()

            elif selection == "4":
                self.check_balance()

            elif selection == "5":
                self.mini_statement()

            else:
                print("Invalid selection.")
            option = int(input("1.MAIN MENU\n2.EXIT:"))
            if option == 2:
                print("Thank You")
                break
                               

    def start(self):

        print("Please insert your ATM card.")

        if self.verify_pin():
            print(f"Welcome, {self.name}!")
            self.atm_menu()


atm = ATM()
atm.start()
