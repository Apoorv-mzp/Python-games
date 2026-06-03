import random

print("🎮 Welcome to Number Guessing Game!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low! Try again.")

    elif guess > secret_number:
        print("📈 Too High! Try again.")

    else:
        print("🎉 Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break