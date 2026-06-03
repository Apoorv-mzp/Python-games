# Attendence managent system

print("\n------------Welcome to the Attendence Management System-------------")
students = {}
while True:
    print("\n1. Add Student")
    print("\n2. Mark Attendence")
    print("\n3. View Attendence")
    print("\n4. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        name = input("\nEnter the student's name: ")
        students[name] = []
        print(f"{name} has been added to the system.")
    elif choice == 2:
        name = input("Enter the student's name: ")
        if name in students:
            students[name].append("\nPresent")
            print(f"\n{name}'s attendence has been marked as Present.")
        else:
            print(f"\n{name} is not in the system. Please add the student first.")
    elif choice == 3:
        name = input("Enter the student's name: ")
        if name in students:
            attendence_count = len(students[name])
            print(f"\n{name} has been marked present {attendence_count} times.")
        else:
            print(f"\n{name} is not in the system. Please add the student first.")
    elif choice == 4:
        print("\nThank you for using the Attendence Management System. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")