print('Welcome to ATM using Python.')

balance = 5000
chance = 3

while chance > 0:
    a = int(input("Enter your ATM pin ->> "))

    if a == 231001:
        print(" ATM unlocked")

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = int(input("Enter your choice ->> "))

            if choice == 1:
                print(" Your current balance is ->>", balance)

            elif choice == 2:
                b = int(input("How much money you want to withdraw? ->> "))

                if b <= 0:
                    print(" Invalid amount")

                elif b > balance:
                    print("Insufficient balance")

                else:
                    balance -= b
                    print(" Withdrawal successful")
                    print(" Remaining balance:", balance)

            elif choice == 3:
                c = int(input("How much money you want to deposit? ->> "))

                if c <= 0:
                    print("Invalid deposit amount")

                else:
                    balance += c
                    print(" Money deposited successfully")
                    print(" New balance:", balance)

            elif choice == 4:
                print("Thanks for using Python ATM")
                break

            else:
                print(" Invalid choice")

        break

    else:
        chance -= 1
        print(" Wrong PIN")

        if chance > 0:
            print(" Attempts left:", chance)

        else:
            print(" ATM Blocked")