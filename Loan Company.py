print("------------WELCOME TO LOAN_BY_APOORV-------------")

users = {}

while True:

    print("\n---------MAIN MENU----------")
    print("1. Create Account")

    print("2. Login")

    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("\n---------CREATE ACCOUNT---------")

        name = input("Enter your name: ")

        age = int(input("Enter your age: "))

        salary = int(input("Enter your salary: "))

        phone = input("Enter your phone number: ")

        username = input("Create username: ")

        password = input("Create password: ")

        users[username] = {

            "name": name,

            "age": age,

            "salary": salary,

            "phone": phone,

            "password": password,

            "balance": 1000
        }

        print("✅ Account Created Successfully!")

    elif choice == 2:

        print("\n---------LOGIN---------")

        username = input("Enter username: ")

        password = input("Enter password: ")

        if username in users and users[username]["password"] == password:

            print("✅ Login Successful!")

            while True:

                print("\n---------USER MENU---------")

                print("1. View Profile")

                print("2. Withdraw Money")

                print("3. Check Balance")

                print("4. Logout")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:

                    print("\n---------PROFILE---------")

                    print("Name:", users[username]["name"])

                    print("Age:", users[username]["age"])

                    print("Salary:", users[username]["salary"])

                    print("Phone:", users[username]["phone"])

                elif user_choice == 2:

                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= users[username]["balance"]:

                        users[username]["balance"] -= amount

                        print("✅ Money Withdrawn Successfully!")

                    else:

                        print("❌ Insufficient Balance!")

                elif user_choice == 3:

                    print("Current Balance:", users[username]["balance"])

                elif user_choice == 4:

                    print("✅ Logged Out Successfully!")
                    break

                else:
                    print("❌ Invalid Choice!")

        else:
            print("❌ Wrong Username or Password!")

    elif choice == 3:

        print("Thank you for using LOAN_BY_APOORV ❤️")

        break

    else:
        
        print("❌ Invalid Choice!")