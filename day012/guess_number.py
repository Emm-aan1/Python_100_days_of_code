from art import logo
import random

print(logo)


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        print(f"You have {lives} lives remaining.")
        guess = int(input("Make a guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number '{secret_number}' correctly.")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        lives -= 1

        if lives == 0:
            print(f"You've run out of lives! The number was {secret_number}. Better luck next time!")


number_guessing_game()
