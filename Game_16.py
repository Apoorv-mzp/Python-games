
import random
word_list = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']
selected_word = random.choice(word_list)
print("Welcome to the Word Guessing Game!")
print("You have selected a word from the list.")
print("You have 5 attempts to guess the correct word.")
attempts = 5
for attempt in range(1, attempts + 1):
    guess = input(f"Attempt {attempt}: Enter your guess: ").lower()
    if guess < selected_word:
        print("Your guess comes before the word alphabetically. Try again.")
    elif guess > selected_word:
        print("Your guess comes after the word alphabetically. Try again.")
    else:
        print(f"Congratulations! You've guessed the correct word '{selected_word}' in {attempt} attempts.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct word was '{selected_word}'.")
print("Thank you for playing the Word Guessing Game. Goodbye!")
print("Press 's' to start the game or 'q' to quit.")
start_choice = input().lower()
if start_choice == 's':
    # The game starts automatically above
    pass
elif start_choice == 'q':
    print("Thank you for playing! bye-bye.")