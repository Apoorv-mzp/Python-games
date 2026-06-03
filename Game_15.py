print("-----------WELCOME TO MARKSHEET GENERATOR------------")

a= input('\nEnter the name of student:')

g= input('\nEnter the class of student:')

i= int(input('\nEnter the roll no. of student:'))

b= int(input('\nEnter the maths marks of student:'))

c= int(input('\nEnter the science marks of student:'))

d= int(input('\nEnter the  english marks of student:'))

e= int(input('\nEnter the computer marks of student:'))

f= int(input('\nEnter the hindi marks of the student:'))

j= int(input('\nEnter the total marks of the student:'))

k= int(input('\nEnter the percentage of the student:'))

print('----------MARKSHEET OF STUDENT----------')
print('\nName of the student:', a)

print('\nClass of the student:', g)

print('\nRoll no. of the student:', i)

print('\nMaths marks: {}/100'.format(b))

print('\nScience marks: {}/100'.format(c))

print('\nEnglish marks: {}/100'.format(d))

print('\nComputer marks: {}/100'.format(e))

print('\nHindi marks: {}/100'.format(f))

print('\nTotal marks: {}/500'.format(j))

print('\nPercentage: {}%'.format(k))

print('\n🥳🥳🎊🎊-------Congratulations for scoring {}% in class exams 🎊🎊!🥳🥳-------'.format(a, k))
