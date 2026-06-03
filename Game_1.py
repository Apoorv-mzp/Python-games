print('--------Welcome to the marks calculator----------')
subject1 = int(input('Enter the marks of subject Maths: '))
subject2 = int(input('Enter the marks of subject English: '))
subject3 = int(input('Enter the marks of subject Hindi: '))
subject4 = int(input('Enter the marks of subject Computer: '))
subject5 = int(input('Enter the marks of subject Science: '))
if subject1 > 92 or subject2 > 92 or subject3 > 92 or subject4 > 92 or subject5 > 92:
    print('Marks should not be greater than 92. Please enter valid marks.')
    exit()
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 460) * 100
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
else:
    grade = 'D'
print('--------Certificate of Marks--------')
print(f'Total Marks: {total_marks}')
print(f'Percentage: {percentage:.2f}%')
print(f'Grade: {grade}')
print('\n--------Thank you for using the marks calculator--------')

