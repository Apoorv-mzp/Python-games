
print("Welcome to Password Strength Checker")
password = input("Enter your password: ")
if len(password) < 6:
    print("Password should be at least 6 characters long.")
elif len(password) < 10:
    print("Ok-ok Password you can keep more safe.")
else:
    print("Your password is strong.") 
