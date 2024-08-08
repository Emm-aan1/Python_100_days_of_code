# Day 7: Hangman Game

## Project Overview

On Day 7 of the #100DaysOfCode challenge with Dr. Angela Yu, the focus was on creating a Hangman game using Python. The project involved using loops, conditionals, and list operations to build a fully functional game.

## Hangman Game

### How It Works

1. **Word List:** The game uses a predefined list of words from which a random word is selected.
2. **Initialize Variables:** 
   - A list to keep track of the guessed letters.
   - A variable to count the number of wrong guesses.
   - A variable to store the display state of the word with blanks.
3. **Game Loop:** 
   - Prompt the user to guess a letter.
   - Check if the guessed letter is in the word.
   - Update the display state of the word with correctly guessed letters.
   - If the guessed letter is not in the word, increment the count of wrong guesses.
   - Continue until the word is guessed or the maximum number of wrong guesses is reached.
4. **Output:** Display the final result (win or lose) and the correct word.

### Key Concepts Learned

- **Loops:** Using `for` and `while` loops to iterate through user inputs and game states.
- **Conditionals:** Applying if-else conditions to check guesses and update game status.
- **List Operations:** Manipulating lists to keep track of guessed letters and the display state of the word.
- **Randomization:** Using Python’s `random` module to select a word from the list.

## How to Run

1. Ensure Python is installed on your system.
2. Create a Python file for the Hangman game.
3. Implement the logic as described in the explanations above.
4. Run the program by executing the Python file and follow the prompts.