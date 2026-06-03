print('--------Welcome to the ATM Machine----------')
balance = 1000
while True:
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print(f'Your current balance is: ${balance}')
    elif choice == 2:
        deposit_amount = float(input('Enter the amount to deposit: '))
        balance += deposit_amount
        print(f'You have deposited: ${deposit_amount}')
        print(f'Your new balance is: ${balance}')
    elif choice == 3:
        withdraw_amount = float(input('Enter the amount to withdraw: '))
        if withdraw_amount > balance:
            print('Insufficient funds. Please try again.')
        else:
            balance -= withdraw_amount
            print(f'You have withdrawn: rs{withdraw_amount}')
            print(f'Your new balance is: rs{balance}')
    elif choice == 4:
        print('Thank you for using the ATM Machine. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
