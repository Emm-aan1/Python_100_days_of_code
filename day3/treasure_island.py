print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
print("Choose a path 🚶🏾‍♀️🚶🏾🚶🏾‍♂️")

while True:
    user_choice = input("Where do you wanna go? Type 'left' or 'right'?\n").strip().lower()
    if user_choice == 'right':
        print("You fell into a spike trap. Game Over 😢")
        break
    elif user_choice == 'left':
        print("You arrived at the lake.")
        user_choice = input("Do you want to 'Swim' or 'Wait'?\n").strip().lower()
        if user_choice == 'swim':
            print("You were attacked by lake monsters 👾. Game Over 😢")
            break
        elif user_choice == 'wait':
            print("The boat has arrived, sailing over...🚣🏾")
            user_choice = input("Which door do you choose? 'Blue', 'Yellow', or 'Red'?\n").strip().lower()
            if user_choice == 'red':
                print("You entered a monster den 🧌. Game Over 😢")
                break
            elif user_choice == 'blue':
                print("You fell into a cage and lost. Game Over 😢")
                break
            elif user_choice == 'yellow':
                print("You found the treasure. You won 🪙")
                break
            else:
                print("Invalid choice, you died 💀.")
                break
        else:
            print("Invalid choice, you died 💀.")
            break
    else:
        print("Invalid: Please select 'left' or 'right'.")
