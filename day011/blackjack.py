from art import logo
import random

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def create_deck():
    """Create a deck by randomly picking a card value."""
    return random.choice(card_values)


def calculate_hand_value(hand):
    """Calculate the value of a hand, adjusting for aces."""
    value = sum(hand)
    num_aces = hand.count(11)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


def display_hands(user_hand, comp_hand, reveal_comp=False):
    """Display the hands of the user and the computer."""
    print(f"Your cards: {user_hand}, current score: {calculate_hand_value(user_hand)}")
    if reveal_comp:
        print(f"Computer's cards: {comp_hand}, score: {calculate_hand_value(comp_hand)}")
    else:
        print(f"Computer's cards: {comp_hand[0]}, [Hidden]")


def play_blackjack():
    """Play a single game of Blackjack."""
    print(logo)
    print("Welcome to Blackjack!")

    user_hand = [create_deck() for _ in range(2)]
    comp_hand = [create_deck() for _ in range(2)]

    game_over = False

    while not game_over:
        display_hands(user_hand, comp_hand)

        user_score = calculate_hand_value(user_hand)
        comp_score = calculate_hand_value(comp_hand)

        if user_score == 21 and len(user_hand) == 2:
            print("Blackjack! You win!")
            return
        elif user_score > 21:
            print("You bust! Computer wins.")
            return

        action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if action == 'y':
            user_hand.append(create_deck())
        else:
            game_over = True

    while calculate_hand_value(comp_hand) < 17:
        comp_hand.append(create_deck())

    display_hands(user_hand, comp_hand, reveal_comp=True)

    user_score = calculate_hand_value(user_hand)
    comp_score = calculate_hand_value(comp_hand)

    if comp_score > 21:
        print("Computer busts! You win!")
    elif comp_score > user_score:
        print("Computer wins!")
    elif comp_score < user_score:
        print("You win!")
    else:
        print("It's a draw!")


def main():
    while True:
        play_blackjack()
        if input("Do you want to play again? [Y/N] ").lower() != 'y':
            break


if __name__ == "__main__":
    main()
