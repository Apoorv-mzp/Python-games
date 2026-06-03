print('------------WELCOME TO APOORV SHOP!-------------')

print('1- Apple  - Rs20')
print('2- Banana - Rs50')
print('3- Orange - Rs80')
print('4- Mango  - Rs40')
print('5- Grapes - Rs150')
print('6- Jamun  - Rs200')

total = 0

# Apple
a = int(input("\nDo you want to buy Apple? (Yes=1 / No=2): "))
if a == 1:
    g = int(input("How many Apples do you want to buy? "))
    total += g * 20
    print("Apple added to cart!")
else:
    g = 0

# Banana
b = int(input("\nDo you want to buy Banana? (Yes=1 / No=2): "))
if b == 1:
    h = int(input("How many Bananas do you want to buy? "))
    total += h * 50
    print("Banana added to cart!")
else:
    h = 0

# Orange
c = int(input("\nDo you want to buy Orange? (Yes=1 / No=2): "))
if c == 1:
    i = int(input("How many Oranges do you want to buy? "))
    total += i * 80
    print("Orange added to cart!")
else:
    i = 0

# Mango
d = int(input("\nDo you want to buy Mango? (Yes=1 / No=2): "))
if d == 1:
    j = int(input("How many Mangos do you want to buy? "))

    if j > 2:
        print("You can buy only 2 Mangos!")
        j = 2

    total += j * 40
    print("Mango added to cart!")
else:
    j = 0

# Grapes
e = int(input("\nDo you want to buy Grapes? (Yes=1 / No=2): "))
if e == 1:
    k = int(input("How many Grapes do you want to buy? "))
    total += k * 150
    print("Grapes added to cart!")
else:
    k = 0

# Jamun
f = int(input("\nDo you want to buy Jamun? (Yes=1 / No=2): "))
if f == 1:
    l = int(input("How many Jamuns do you want to buy? "))
    total += l * 200
    print("Jamun added to cart!")
else:
    l = 0

# Final Bill
print("\n========== BILL ==========")

if g > 0:
    print("Apple  x", g, "=", g * 20)

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