print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

lovers = name1 + name2
true_count = lovers.count('t') + lovers.count('r') + lovers.count('u') + lovers.count('e')
love_count = lovers.count('l') + lovers.count('o') + lovers.count('v') + lovers.count('e')

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 60:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}, you are perfect together.")
