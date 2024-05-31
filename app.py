# a rock paper scissors game using python with GitHub Copilot

# create random module to simulate computer’s actions
import random

# create dictionary to define the winning conditions using "rock": "paper": "scissors": scenarios and compare the user’s choice with the computer’s choice to determine the winner
def main():
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    user_action = input("Enter a choice (rock, paper, scissors): ")
    computer_action = random.choice(["rock", "paper", "scissors"])

    if user_action == computer_action:
        result = "It's a tie!"
    elif rules[user_action] == computer_action:
        result = "You win!"
    else:
        result = "Computer wins!"

    print(f"Computer chose {computer_action}. {result}")

if __name__ == "__main__":
    main()



