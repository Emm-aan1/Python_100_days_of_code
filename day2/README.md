# Day 2: Understanding Data Types and Manipulating Strings

## Project Overview

On Day 2 of the #100DaysOfCode challenge with Dr. Angela Yu, the focus was on understanding data types and how to manipulate strings. The task involved creating a simple program to calculate the amount each person needs to pay when splitting a bill, including a tip.

## Project Details

### Problem Statement

Given:
- A total bill amount.
- The percentage of tip to be added.
- The number of people splitting the bill.

The program calculates how much each person should pay, including their share of the tip, and formats the result to two decimal places.

### Code Implementation

```python
print("Welcome to Dilaro's Restaurant")
bill = float(input("Enter your bill: $"))
tip_percentage = float(input("How much tips? 5%, 7%, or 10%? ")) / 100

total_tip = bill * tip_percentage
split_bill = int(input("How many people are splitting the bill? "))

total_bill = (bill + total_tip) / split_bill
formatted_bill = "{:.2f}".format(total_bill)
print(f"Each person will pay: ${formatted_bill}")
print("Thank you")
```

### Key Concepts Learned

- **Data Types:** Understanding different data types such as integers, floats, and strings.
- **User Input:** Using `input()` to capture user input and converting it to appropriate data types.
- **Arithmetic Operations:** Performing arithmetic calculations to determine the tip amount and split the bill.
- **String Formatting:** Formatting the result to two decimal places using `round()` and `format()` methods.

### How to Run the Program

1. Ensure you have Python installed on your system.
2. Copy the code into a Python file (e.g., `bill_splitter.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory containing your Python file.
5. Run the program by typing `python bill_splitter.py` and follow the prompts.

### Reflection

Today, I deepened my understanding of data types and string manipulation in Python. It was insightful to learn how to handle user inputs and format outputs. This exercise provided a practical way to apply these concepts, and I'm looking forward to building more complex programs in the future.
