print('🙏🏻 Welcome to ATM using Python 🐍')
# This will print the welcome message.

balance = 5000
# This variable stores the current balance of the ATM account.

ATM_pin = 1234
# This variable stores the ATM PIN used to unlock the ATM.

chance = 3
# This variable stores how many chances the user has to enter the correct PIN.

while chance > 0:
# This loop will keep running until chances become 0.

    pin = int(input("Please enter the ATM pin to unlock ->> "))
    # This line takes PIN input from the user.

    if pin == ATM_pin:
    # This condition checks whether the entered PIN is correct or not.

        print('✅ ATM unlocked successfully.')
        # This message will print if the PIN is correct.

        while True:
        # This infinite loop keeps showing the ATM menu until user exits.

            print("\n====== ATM MENU ======")
            # This prints the ATM menu heading.

            print("1. Check Balance")
            # Option 1 is used to check balance.

            print("2. Withdraw Money")
            # Option 2 is used to withdraw money.

            print("3. Deposit Money")
            # Option 3 is used to deposit money.

            print("4. Exit")
            # Option 4 is used to exit the ATM.

            choice = int(input("Enter your choice ->> "))
            # This line takes menu choice input from the user.

            if choice == 1:
            # This condition runs when user chooses option 1.

                print("💰 Your Current Balance is ->>", balance)
                # This prints the current balance.

            elif choice == 2:
            # This condition runs when user chooses option 2.

                withdraw = int(input("How much money do you want to withdraw? ->> "))
                # This line takes withdrawal amount from the user.

                if withdraw <= 0:
                # This checks if the entered amount is invalid.

                    print("❌ Invalid Amount")
                    # This prints when amount is less than or equal to 0.

                elif withdraw > balance:
                # This checks whether withdrawal amount is greater than balance.

                    print("❌ Insufficient Balance")
                    # This prints when balance is insufficient.

                else:
                # This block runs when withdrawal amount is valid.

                    balance -= withdraw
                    # This subtracts withdrawal money from balance.

                    print("✅ Withdrawal Successful")
                    # This prints when withdrawal is successful.

                    print("💰 Remaining Balance ->>", balance)
                    # This shows the remaining balance.

            elif choice == 3:
            # This condition runs when user chooses option 3.

                deposit = int(input("How much money do you want to deposit? ->> "))
                # This line takes deposit amount from the user.

                if deposit <= 0:
                # This checks if deposit amount is invalid.

                    print("❌ Invalid Deposit Amount")
                    # This prints when deposit amount is invalid.

                else:
                # This block runs when deposit amount is valid.

                    balance += deposit
                    # This adds deposit money to the balance.

                    print("✅ Money Deposited Successfully")
                    # This prints when money is deposited successfully.

                    print("💰 Updated Balance ->>", balance)
                    # This prints the updated balance.

            elif choice == 4:
            # This condition runs when user chooses Exit option.

                print("🙏🏻 Thanks for using Python ATM.")
                # This prints thank you message.

                break
                # This breaks the ATM menu loop and exits program.

            else:
            # This condition runs when user enters invalid menu option.

                print("❌ Invalid Choice")
                # This prints invalid choice message.

        break
        # This breaks the PIN loop after successful ATM usage.

    else:
    # This block runs when user enters wrong PIN.

        chance -= 1
        # This decreases remaining chances by 1.

        print("❌ Wrong PIN")
        # This prints wrong PIN message.

        if chance > 0:
        # This condition checks whether attempts are still left.

            print("🔁 Attempts left ->>", chance)
            # This prints remaining attempts.

        else:
        # This condition runs when all attempts are finished.

            print("🚫 ATM Blocked")
            # This prints ATM blocked message.