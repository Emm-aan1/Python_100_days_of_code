import random
from hangman_art import art, logo

print(logo)

lives = 6
word_list = ["python", "hangman", "programming", "computer", "apple", "banana", "orange", "grape", "cat",
             "dog", "fish", "bird", "table", "chair", "book", "pen", "pencil", "paper", "cloud", "mountain"]

chosen_word = random.choice(word_list)

placeholder = ''
for word in chosen_word:
    placeholder += '_'
print(placeholder)

game_guessed = False
all_words = []

while not game_guessed:
    guess = input("Guess the word: ").lower()
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            all_words.append(letter)
        elif letter in all_words:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_guessed = True
            # print("Game Over")
    else:
        print("You already guessed it")

    print(art[lives])
    print(f"You have {lives} lives left")

    if '_' not in display:
        game_guessed = True
        print("You guessed all word")
