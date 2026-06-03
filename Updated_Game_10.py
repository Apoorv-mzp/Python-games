print('------------WELCOME TO APOORV SHOP!-------------')
print('1- Apple  - Rs20')
print('2- Banana - Rs50')
print('3- Orange - Rs80')
print('4- Mango  - Rs40')
print('5- Grapes - Rs150')
print('6- Jamun  - Rs200')
total = 0
a = int(input("\nDo you want to buy Apple? (Yes=1 / No=2): "))
if a > 2:
    print('You can\'t buy apple more than 2.')
    ab = 0
else:
    ab = int(input("How many Apples do you want to buy? "))
    if ab > 2:
        print('You can\'t buy apple more than 2.')
        z = int(input('Do you want to buy 2 Apples? (Yes=1 / No=2): '))
        if z == 1:
            ab = 2
            print("Okk! Apple added to cart.")
        else:
            print("Apple not added to cart!")
            ab = 0
    total += ab * 20
b = int(input("\nDo you want to buy Banana? (Yes=1 / No=2): "))
if b == 1:
    h = int(input("How many Bananas do you want to buy? "))
    total += h * 50
    print("Banana added to cart!")
else:
    h = 0
c = int(input("\nDo you want to buy Orange? (Yes=1 / No=2): "))
if c == 1:
    i = int(input("How many Oranges do you want to buy? "))
    total += i * 80
    print("Orange added to cart!")
else:
    i = 0
d = int(input("\nDo you want to buy Mango? (Yes=1 / No=2): "))
if d == 1:
    j = int(input("How many Mangos do you want to buy? "))
    if j > 2:
        print("You can buy only 2 Mangos!")
        z = int(input('Do you want to buy 2 Mangos? (Yes=1 / No=2): '))
        if z == 1:
            j = 2
            print("Okk!")
        else:
            print("Mango not added to cart!")
            j = 0
    total += j * 40
    print("Mango added to cart!")
else:
    j = 0
e = int(input("\nDo you want to buy Grapes? (Yes=1 / No=2): "))
if e == 1:
    k = int(input("How many Grapes do you want to buy? "))
    total += k * 150
    print("Grapes added to cart!")
else:
    k = 0
f = int(input("\nDo you want to buy Jamun? (Yes=1 / No=2): "))
if f == 1:
    l = int(input("How many Jamuns do you want to buy? "))
    total += l * 200
    print("Jamun added to cart!")
else:
    l = 0
fruit_count = 0
if ab > 0:
    fruit_count += 1
if h > 0:
    fruit_count += 1
if i > 0:
    fruit_count += 1
if j > 0:
    fruit_count += 1
if k > 0:
    fruit_count += 1
if l > 0:
    fruit_count += 1
if fruit_count > 3 and ab > 0 and j > 0:
    print("\n❌ More than 3 fruit types selected.")
    print("You can buy either Apple OR Mango, not both.")
    choice = int(input("Keep Apple (1) or Mango (2)? : "))
    if choice == 1:
        total -= j * 40
        j = 0
        print("Mango removed from cart.")
    elif choice == 2:
        total -= ab * 20
        ab = 0
        print("Apple removed from cart.")
print("\n========== BILL ==========")
if ab > 0:
    print("Apple  x", ab, "=", ab * 20)
if h > 0:
    print("Banana x", h, "=", h * 50)
if i > 0:
    print("Orange x", i, "=", i * 80)
if j > 0:
    print("Mango  x", j, "=", j * 40)
if k > 0:
    print("Grapes x", k, "=", k * 150)
if l > 0:
    print("Jamun  x", l, "=", l * 200)
print("--------------------------")
print("Total Bill = Rs", total)
print("Thank you for shopping at Apoorv Shop! 😊")