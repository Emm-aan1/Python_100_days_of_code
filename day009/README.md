# Day 9: Dictionaries and Nesting

## Project Overview

On Day 9 of the #100DaysOfCode challenge with Dr. Angela Yu, the focus was on working with dictionaries and nesting in Python. The exercise for the day involved creating a secret auction program that allows multiple users to place bids and determines the highest bidder.

## Secret Auction

### How It Works

1. **Importing Assets:**
   - The program starts by importing and displaying an ASCII art logo for the auction.

2. **Bid Collection:**
   - The program prompts each user to enter their name and bid amount.
   - It stores the name and bid in a dictionary where the user's name is the key and the bid amount is the value.

3. **Looping Through Bidders:**
   - After each bid, the program asks if there are other bidders.
   - If there are more bidders, the program continues to collect bids.
   - If there are no more bidders, the bidding process ends.

4. **Determining the Winner:**
   - A function named `highest_bidder` is used to iterate through the dictionary of bids to find the highest bid and the corresponding bidder's name.
   - The program then announces the winner and their winning bid.

### Key Concepts Learned

- **Dictionaries:** Using dictionaries to store and retrieve key-value pairs, where the key is the bidder's name and the value is their bid amount.
- **Nesting:** Understanding how to structure and access nested data within dictionaries.
- **Function Creation:** Defining a function to determine the highest bid and the corresponding winner.
- **Conditionals:** Using if-else statements to control the flow of the bidding process based on user input.

## How to Run

1. Ensure Python is installed on your system.
2. Create a Python file for the secret auction program.
3. Implement the logic as described in the explanations above.
4. Run the program by executing the Python file, and follow the prompts to place bids and determine the highest bidder.
