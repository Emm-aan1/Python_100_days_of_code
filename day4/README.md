## Day 4: Randomization and Python Lists

## Project Overview

On Day 4 of the #100DaysOfCode challenge with Dr. Angela Yu, the focus was on randomization and Python lists. The exercises involved using Python's `random` module and list operations to solve different problems.

## Exercises

### 1. Heads or Tails

This exercise simulates a coin toss. The program randomly selects between "heads" and "tails" to simulate the result of a coin flip.

### How It Works

1. **Random Choice:** Use Python's `random.randint()` method to randomly select between "heads" and "tails."
2. **Output:** Display the result of the coin toss to the user.

### 2. Banker Roulette

This exercise simulates a random selection of a person from a group to pay for a meal. The program allows users to add names to a list and then randomly selects one person to pay.

### How It Works

1. **Name Input:** Allow users to input names to be added to a list.
2. **Random Selection:** Use `random.randint()` to randomly select a name from the list.
3. **Output:** Display the name of the person who will pay for the meal.

### 3. Rock, Paper, Scissors

This exercise implements the classic game of Rock, Paper, Scissors. The user plays against the computer, and the program determines the winner based on the rules of the game.

### How It Works

1. **User Choice:** Capture the user's choice of "rock," "paper," or "scissors."
2. **Computer Choice:** Use `random.choice()` to select the computer's choice.
3. **Determine Winner:** Compare the user's choice and the computer's choice to determine the winner based on the rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
4. **Output:** Display the choices of both the user and the computer, and announce the winner.

## Key Concepts Learned

- **Randomization:** Using Python’s `random` module to generate random results.
- **Lists:** Creating and manipulating lists to store names and game options.
- **Conditionals:** Implementing decision-making logic to determine the winner in Rock, Paper, Scissors and to handle user input.

## How to Run

1. Ensure Python is installed on your system.
2. Create Python files for each exercise.
3. Implement the logic as described in the explanations above.
4. Run each program by executing the Python files and follow the prompts.

## Reflection

Today's exercises provided practical experience with randomization and list operations in Python. Implementing these features reinforced the understanding of how to handle random events and manage data using lists, which are fundamental skills in Python programming.
