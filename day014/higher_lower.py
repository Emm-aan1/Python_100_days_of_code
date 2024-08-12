import random
from game_data import data
from art import logo, vs

def format_data(account):
    """Format account data into printable format."""
    name = account["name"]
    description = account["description"]
    return f"{name}, a/an {description}"

def compare_accounts(account_a, account_b):
    """Compares two accounts based on follower count."""
    if account_a["followers"] > account_b["followers"]:
        return "A"
    else:
        return "B"

def game():
    user_score = 0

    # Initialize account_a outside the loop
    account_a = None

    while True:
        if user_score > 0:
            pass  # No need to re-assign account_a here, it's already set from the previous loop
        else:
            account_a = random.choice(data)

        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(logo)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        correct_answer = compare_accounts(account_a, account_b)

        if user_choice == correct_answer:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            break

game()
