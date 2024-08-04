import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock, Paper and Scissors game")
user_score = 0

while True:
    start_game = input("\nUser 👤 vs Computer 🤖 \nPlay Game. 'Yes' or 'No'\n").lower()

    if start_game == 'yes':
        game = [rock, paper, scissors]
        game_choice = input("Enter 0 for Rock, 1 for Paper and 2 for Scissors\n")
        user1 = int(game_choice)
        comp1 = random.randint(0, 2)

        print(f"You chose: {game[user1]}\n")
        print(f"Computer chose:\n{game[comp1]}\n")

        if user1 == comp1:
            print("It's a tie!")
        elif user1 == 0 and comp1 == 1:
            print("Computer wins!")
        elif user1 == 0 and comp1 == 2:
            print("You win!")
        elif user1 == 1 and comp1 == 0:
            print("You win!")
        elif user1 == 1 and comp1 == 2:
            print("Computer wins!")
        elif user1 == 2 and comp1 == 0:
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Thank you. Try again later.")
        break
