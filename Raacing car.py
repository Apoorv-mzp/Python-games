print("🏎️ -------- WELCOME TO CAR RACING CAREER GAME -------- 🏎️")

users = {}

while True:

    print("\n--------- MAIN MENU ---------")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("\n--------- CREATE ACCOUNT ---------")

        name = input("Enter your name: ")
        username = input("Create username: ")
        password = input("Create password: ")

        users[username] = {
            "name": name,
            "password": password,
            "money": 5000,
            "car": "Basic Car",
            "wins": 0
        }

        print("✅ Account Created Successfully!")

    elif choice == 2:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username]["password"] == password:

            print("✅ Login Successful!")

            while True:

                print("\n--------- PLAYER MENU ---------")
                print("1. View Profile")
                print("2. Race")
                print("3. Upgrade Car")
                print("4. Check Money")
                print("5. Logout")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:

                    print("\n------ PROFILE ------")
                    print("Name:", users[username]["name"])
                    print("Car:", users[username]["car"])
                    print("Wins:", users[username]["wins"])
                    print("Money: ₹", users[username]["money"])

                elif user_choice == 2:

                    print("\n🏁 Race Started!")

                    race_result = input(
                        "Did you win the race? (yes/no): "
                    ).lower()

                    if race_result == "yes":
                        users[username]["money"] += 2000
                        users[username]["wins"] += 1

                        print("🎉 You won the race!")
                        print("💰 ₹2000 added.")

                    else:
                        print("😢 You lost the race.")

                elif user_choice == 3:

                    print("\n------ GARAGE ------")
                    print("1. Sports Car (₹5000)")
                    print("2. Super Car (₹10000)")

                    car_choice = int(input("Choose car: "))

                    if car_choice == 1:

                        if users[username]["money"] >= 5000:

                            users[username]["money"] -= 5000
                            users[username]["car"] = "Sports Car"

                            print("✅ Sports Car Purchased!")

                        else:
                            print("❌ Not enough money!")

                    elif car_choice == 2:

                        if users[username]["money"] >= 10000:

                            users[username]["money"] -= 10000
                            users[username]["car"] = "Super Car"

                            print("✅ Super Car Purchased!")

                        else:
                            print("❌ Not enough money!")

                elif user_choice == 4:

                    print("💰 Current Money: ₹",
                          users[username]["money"])

                elif user_choice == 5:

                    print("✅ Logged Out Successfully!")
                    break

                else:
                    print("❌ Invalid Choice!")

        else:
            print("❌ Wrong Username or Password!")

    elif choice == 3:

        print("🏁 Thank you for playing CAR RACING CAREER GAME!")
        break

    else:
        print("❌ Invalid Choice!")