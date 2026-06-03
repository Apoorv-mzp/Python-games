import random

def voting_game():
    print("Welcome to the Yes or No Voting Game!")
    
    questions = [
        "Do you like Python programming?",
        "Is the sky blue?",
        "Do you enjoy outdoor activities?",
        "Is pizza your favorite food?",
        "Do you like to travel?"
    ]
    
    user_score = 0
    computer_score = 0
    
    for question in questions:
        print("\n" + question)
        user_vote = input("Enter your vote (yes/no): ").lower()
        
        if user_vote not in ['yes', 'no']:
            print("Invalid vote! Question skipped.")
            continue
        
        computer_vote = random.choice(['yes', 'no'])
        print(f"Computer voted: {computer_vote}")
        
        if user_vote == computer_vote:
            print("It's a tie!")
        else:
            print("You win this question!")
            user_score += 1

    print("\nFinal Score:")
    print("You:", user_score)
    print("Computer:", computer_score)

voting_game()
