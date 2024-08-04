import random

print("Welcome to the Banker Roulette 😈. Add a name on the list to play")
names = []

while True:
    add_name = input("Do you want to add name? 'Yes' or 'No'?\n").strip().lower()

    if add_name == 'yes':
        user_name = input("What's your name?\n")
        names.append(user_name)

    elif add_name == 'no':
        break

    else:
        print("Invalid response, please select 'Yes' or 'No'.")

if names:
    get_player = random.randint(0, len(names) - 1)
    print(f"{names[get_player]} is going to buy the meal today")

else:
    print("No names added.")