print('\n---------WELCOME TO BLOOMERS SCHOOL-------------')

print('\n----------OUR TOPPERS----------')

print('\n-------Highest Percentage--------')

print('Apoorv Percentage- 100% Apoorv marks- 1000/1000')
print('-------')
print('Aayush Percentage- 98.2% Aayush marks- 970/1000')
print('-------')
print('Roshan Percentage- 97.22% Roshan marks- 915/1000')
print('-------')
print('Rohan Percentage- 95.2% Rohan marks- 910/1000')
print('-------')
print('Rahul Percentage- 92.82 % Rahul marks- 890/1000')
print('\n----------------------')

print('\n--------Higest Attendence---------')

print('Apoorv Attendence- 100%')
print('Aayush Attendence- 97%')
print('Roshan Attendence- 96%')
print('Rohanl Attendence- 95%')
print('Rahul Attendence- 90%')
print('\n---------------------')

print('\n----------Highest Marks----------')

print('Apoorv Marks- 1000/1000')
print('Aayush Marks- 970/1000')
print('Roshan Marks- 915/1000 ')
print('Rohan Marks- 910/1000')
print('Rahul Marks- 890/1000')
print('\n--------------------')

print('-----------Highest Rank-----------')

print('Apoorv Rank- 1st')
print('Aayush Rank- 2nd')
print('Roshan Rank- 3rd')
print('Rohan Rank- 4th')
print('Rahul Rank- 5th ')
print('\n--------------------')
students = {
    "Rahul": {
        "class": 10,
        "roll": 1010,
        "percentage": "92.82%",
        "rank": "5",
        "attendance": "90%",
        "marks": "890/1000",
        "sports": "Cricket"
    },

    "Rohan": {
        "class": 10,
        "roll": 1050,
        "percentage": "95.2%",
        "rank": "4",
        "attendance": "95%",
        "marks": "910/1000",
        "sports": "Cricket"
    },

    "Roshan": {
        "class": 12,
        "roll": 1000,
        "percentage": "97.22%",
        "rank": "3",
        "attendance": "96%",
        "marks": "915/1000",
        "sports": "Football"
    },

    "Aayush": {
        "class": 10,
        "roll": 1244,
        "percentage": "98.2%",
        "rank": "2",
        "attendance": "97%",
        "marks": "970/1000",
        "sports": "Cricket"
    },

    "Apoorv": {
        "class": 7,
        "roll": 90,
        "percentage": "100%",
        "rank": "1",
        "attendance": "100%",
        "marks": "1000/1000",
        "sports": "Cricket"
    }
}

name = input("\nEnter student name -> ").title()
student_class = int(input("Enter student class -> "))
roll = int(input("Enter student roll.no -> "))

if name in students:
    student = students[name]

    if student_class == student["class"] and roll == student["roll"]:

        print(f"\n{name} Information Found Successfully!")

        while True:
            print("\n------ MENU ------")
            print("1. Percentage")
            print("2. Rank")
            print("3. Attendance")
            print("4. Marks")
            print("5. Sports")
            print("6. Exit")

            choice = input("Enter your choice -> ")

            if choice == "1":
                print("Percentage ->", student["percentage"])

            elif choice == "2":
                print("Rank ->", student["rank"])

            elif choice == "3":
                print("Attendance ->", student["attendance"])

            elif choice == "4":
                print("Marks ->", student["marks"])

            elif choice == "5":
                print("Sports ->", student["sports"])

            elif choice == "6":
                print("Thank you for using Bloomers School Portal!")
                break

            else:
                print("Invalid Choice!")

    else:
        print("Class or Roll Number is Incorrect!")

else:
    print("Student Not Found!")