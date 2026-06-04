print("--------------------SCHOOL TIMETABLE GENERATOR--------------------")

name = input("\nEnter Student Name: ")

print(f"\nHello {name} 👋")

print("\nChoose a day to see your timetable.")

print("""
1. Monday
      
2. Tuesday
      
3. Wednesday
      
4. Thursday
      
5. Friday
      
6. Saturday
""")

choice = input("Enter your choice (1-6): ")


if choice == "1":

    print("\n Monday Timetable")

    print("1. Maths")

    print("2. English")

    print("3. Science")

    print("4. Computer")

    print("5. Hindi")


elif choice == "2":

    print("\n Tuesday Timetable")

    print("1. Science")

    print("2. Maths")

    print("3. SST")

    print("4. English")

    print("5. PT")


elif choice == "3":

    print("\n Wednesday Timetable")

    print("1. Computer")

    print("2. Maths")

    print("3. Hindi")

    print("4. Science")

    print("5. Drawing")

elif choice == "4":

    print("\n Thursday Timetable")

    print("1. English")

    print("2. SST")

    print("3. Maths")

    print("4. Computer")

    print("5. Library")

elif choice == "5":

    print("\n Friday Timetable")

    print("1. Science")

    print("2. English")

    print("3. Hindi")

    print("4. Maths")

    print("5. Games")

elif choice == "6":

    print("\n Saturday Timetable")

    print("1. PT")

    print("2. Computer")

    print("3. Art")

    print("4. Music")

    print("5. Holiday Mood 😎")

else:

    print("\n❌ Invalid Choice")

print("\n Thanks for using Timetable Generator")