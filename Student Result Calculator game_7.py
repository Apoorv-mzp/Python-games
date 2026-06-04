
def students_age():
    print("Welcome to the Student Age Guess Game!")
    student_ages = {
        'Alice': 20,
        'Bob': 22,
        'Charlie': 19,
        'David': 21,
        'Eva': 23
    }
    name = input("Enter the student's name (Alice, Bob, Charlie, David, Eva): ")
    if name in student_ages:
        age_guess = int(input(f"Guess the age of {name}: "))
        if age_guess == student_ages[name]:
            print("Correct! You guessed the right age.")
        else:
            print(f"Wrong! The correct age of {name} is {student_ages[name]}.")
    else:
        print("Student not found. Please enter a valid name.")
if __name__ == "__main__":
    students_age()

