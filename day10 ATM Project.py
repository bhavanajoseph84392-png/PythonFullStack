User_Information = {
    "Name": "Bhavana",
    "Mobile Number": " ",
    "ATM PIN": "4400",
    "Balance": 98567,
    "Transaction History": []
}  # User data

print("Please insert your ATM card")

remaining_attempts = 3

while remaining_attempts > 0:

    User_pin = input("ENTER YOUR ATM PIN:")

    if len(User_pin) == 4 and User_pin == User_Information['ATM PIN']:

        print("Welcome to the ATM")

        # HOME PAGE LOOP
        while True:

            User_selection = int(input(
                "\nEnter\n1.Deposit Money \n2.Withdraw Money\n3.Pin Change\n4.Check Balance \n5.Mini Statement\n6.Exit\n"
            ))

            # Deposit
            if User_selection == 1:

                Deposit_Money = int(input("Enter the amount to be deposited: "))

                if Deposit_Money > 1000:

                    if Deposit_Money % 100 == 0:

                        User_Information['Balance'] += Deposit_Money

                        User_Information['Transaction History'].append(
                            f"Deposit:{Deposit_Money}"
                        )

                        print(f"Amount is deposited and Current Balance: {User_Information['Balance']}")

                    else:
                        print("Enter amount in multiples of 100")

                else:
                    print("Minimum deposit should be above 1000")

            # Withdraw
            elif User_selection == 2:

                Withdraw_Money = int(input("Enter the amount to be withdrawn: "))

                if Withdraw_Money <= User_Information['Balance']:

                    if Withdraw_Money % 100 == 0:

                        User_Information['Balance'] -= Withdraw_Money

                        User_Information['Transaction History'].append(
                            f"Withdrawn:{Withdraw_Money}"
                        )

                        print(f"Withdrawal is Successful! New Balance: {User_Information['Balance']}")

                    else:
                        print("Enter amount in multiples of 100")

                else:
                    print("Insufficient Balance")

            # PIN Change
            elif User_selection == 3:

                new_pin = input("Enter your 4-digit PIN:")

                if len(new_pin) == 4 and new_pin.isdigit():

                    User_Information['ATM PIN'] = new_pin

                    print("The PIN has successfully changed")

                else:
                    print("Invalid PIN format. Please enter 4 digits")

            # Check Balance
            elif User_selection == 4:

                print(f"Your Current Balance is: {User_Information['Balance']}")

            # Mini Statement
            elif User_selection == 5:

                print("----Transaction History-----")

                if User_Information['Transaction History'] == []:
                    print("No transactions made")

                else:

                    for i in User_Information['Transaction History']:
                        print(i)

            # Exit
            elif User_selection == 6:

                print("Thank You")
                break

            else:
                print("Invalid Selection")

    else:

        remaining_attempts -= 1

        if remaining_attempts > 0:
            print(f"The remaining attempts are {remaining_attempts}")

        else:
            print("The card gets blocked temporarily")
