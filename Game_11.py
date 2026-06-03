print('\n-----------WELCOME TO SHOBHA APOORV--------------')
print('----Our rooms are available for booking----')

print('\n1. Mumbai')
print('2. Delhi')
print('3. Bangalore')

c = input('\nPlease enter your name to continue: ')

a = int(input('\nEnter your choice to continue: '))

if a == 1:
    print('\nYou have selected Mumbai')
    print('The price of flat is 60,000')

    b = int(input('\nPlease pay the money to the flat owner to get your room with certificate: '))

    if b < 60000:
        print('Please pay the full amount to get your room')

    elif b > 60000:
        print('You have paid more than the required amount')

    else:
        print('Congratulations! You have successfully booked your room in Mumbai')
        print('\nYour Certificate')
        print('------------------SHOBHA APOORV------------------')
        print('Owner Name: Shobha Apoorv')
        print('Customer Name:', c)
        print('Flat: 2BHK')
        print('City: Mumbai')
        print('Price: 60,000')

elif a == 2:
    print('\nYou have selected Delhi')
    print('The price of flat is 50,000')

    b = int(input('\nPlease pay the money to the flat owner to get your room with certificate: '))

    if b < 50000:
        print('Please pay the full amount to get your room')

    elif b > 50000:
        print('You have paid more than the required amount')

    else:
        print('Congratulations! You have successfully booked your room in Delhi')
        print('\nYour Certificate')
        print('------------------SHOBHA APOORV------------------')
        print('Owner Name: Shobha Apoorv')
        print('Customer Name:', c)
        print('Flat: 2BHK')
        print('City: Delhi')
        print('Price: 50,000')

elif a == 3:
    print('\nYou have selected Bangalore')
    print('The price of flat is 40,000')

    b = int(input('\nPlease pay the money to the flat owner to get your room with certificate: '))

    if b < 40000:
        print('Please pay the full amount to get your room')

    elif b > 40000:
        print('You have paid more than the required amount')

    else:
        print('Congratulations! You have successfully booked your room in Bangalore')
        print('\nYour Certificate')
        print('------------------SHOBHA APOORV------------------')
        print('Owner Name: Shobha Apoorv')
        print('Customer Name:', c)
        print('Flat: 2BHK')
        print('City: Bangalore')
        print('Price: 40,000')

else:
    print('\nInvalid Choice!')