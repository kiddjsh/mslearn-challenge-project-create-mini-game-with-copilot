import random

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



