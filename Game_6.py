score = 0

while True:
    number = int(input("\nEnter a number:"))

    if number == 0:
        print(f"Game Over! Your score is {score}")
        break

    guess = input("Will it be Even or Odd? ").lower()

    if number % 2 == 0 and guess == "even":
        print("🎉 Correct!")
        score += 1

    elif number % 2 != 0 and guess == "odd":
        print("🎉 Correct!")
        score += 1

    else:
        print("❌ Wrong!")

print("Final Score:", score)