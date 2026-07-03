class ATM:

    def __init__(self):
        self.user_info = {
            "Name": "Bhavana",
            "Mobile Number": 6436463722,
            "ATM_PIN": "4400",
            "Balance": 98567,
            "Transaction_History": []
        }

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))

        if amount <= 1000 or amount % 100 != 0:
            print("Minimum deposit should be above 1000")
            print("Enter amount in multiples of 100")

        else:
            self.user_info["Balance"] += amount
            self.user_info["Transaction_History"].append(f"Deposit: {amount}")
            print(f"{amount} deposited successfully")

    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn: "))

        if amount > self.user_info["Balance"] or amount % 100 != 0:
            print("Insufficient balance")
            print("Enter amount in multiples of 100")

        else:
            self.user_info["Balance"] -= amount
            self.user_info["Transaction_History"].append(f"Withdraw: {amount}")
            print(f"Withdrawal successful! New balance: {self.user_info['Balance']}")

    def change_pin(self):
        new_pin = input("Enter your new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            self.user_info["ATM_PIN"] = new_pin
            print("PIN changed successfully.")

        else:
            print("Invalid PIN. Please enter exactly 4 digits.")

    def check_balance(self):
        print(f"Your current balance is: {self.user_info['Balance']}")

    def mini_statement(self):
        print("\nTransaction History")

        if not self.user_info["Transaction_History"]:
            print("No transactions yet.")

        else:
            for record in self.user_info["Transaction_History"]:
                print(record)

    def verify_pin(self):
        attempts = 3

        while attempts > 0:

            pin = input("Enter your ATM PIN: ")

            if pin == self.user_info["ATM_PIN"]:
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

            elif selection == "6":
                print("Thank You")
                break

            else:
                print("Invalid selection.")

            option = int(input("1.MAIN MENU\n2.EXIT: "))
            if option == 2:
                print("Thank You")
                break

    def start(self):

        print("Please insert your ATM card.")

        if self.verify_pin():
            print(f"Welcome, {self.user_info['Name']}!")
            self.atm_menu()


atm = ATM()
atm.start()
