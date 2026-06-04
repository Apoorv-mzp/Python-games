print("--------------WELCOME TO GOD APOORV PRO SCHOOL------------------")

teachers = {

    "Apoorv": {

        "age": 30,

        "phone": 9876543210,

        "classes": [1, 2],

        "password": "apoorv123"
    },

    "Rahul": {

        "age": 35,

        "phone": 9876500000,

        "classes": [3, 4],

        "password": "rahul123"
    },

    "Priya": {

        "age": 29,

        "phone": 9876511111,

        "classes": [5, 6],

        "password": "priya123"
    },

    "Neha": {

        "age": 32,

        "phone": 9876522222,

        "classes": [7, 8],

        "password": "neha123"
    }
}

students = {}


while True:

    print("\n========== MAIN MENU ==========")

    print("1. Teacher Login")

    print("2. Student Admission")

    print("3. View Students")

    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n---------- TEACHER LOGIN ----------")

        teacher_name = input("Enter Teacher Name: ")

        password = input("Enter Password: ")

        if teacher_name in teachers:

            if teachers[teacher_name]["password"] == password:

                print("\nLogin Successful ✅")

                print("\nTeacher Name :", teacher_name)
                
                print("Teacher Age :", teachers[teacher_name]["age"])

                print("Phone Number :", teachers[teacher_name]["phone"])

                print("Responsible Classes :",
                      
                      teachers[teacher_name]["classes"])

            else:

                print("Wrong Password ❌")

        else:

            print("Teacher Not Found ❌")


    elif choice == "2":

        print("\n---------- STUDENT ADMISSION FORM ----------")

        student_name = input("Enter Student Name: ")

        age = int(input("Enter Student Age: "))

        student_class = int(input("Enter Student Class: "))

        assigned_teacher = ""


        for teacher in teachers:

            if student_class in teachers[teacher]["classes"]:

                assigned_teacher = teacher

        if assigned_teacher != "":

            students[student_name] = {

                "age": age,

                "class": student_class,

                "teacher": assigned_teacher
            }

            print("\nAdmission Successful ✅")

            print("Student Name :", student_name)

            print("Class :", student_class)

            print("Assigned Teacher :", assigned_teacher)

        else:

            print("No Teacher Available For This Class ❌")

 
    elif choice == "3":

        print("\n---------- ALL STUDENTS ----------")

        if len(students) == 0:

            print("No Students Added Yet ❌")

        else:

            for student in students:

                print("\nStudent Name :", student)

                print("Age :", students[student]["age"])

                print("Class :", students[student]["class"])
                
                print("Teacher :", students[student]["teacher"])


    elif choice == "4":

        print("\nThank You For Using GOD APOORV PRO SCHOOL ❤️")

        break

    else:

        print("Invalid Choice ❌")