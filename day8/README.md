# Day 8: Function Parameters and Caesar Cipher

## Project Overview

On Day 8 of the #100DaysOfCode challenge with Dr. Angela Yu, the focus was on understanding function parameters in Python. The exercise involved implementing a Caesar Cipher, a basic encryption technique.

## Caesar Cipher

### How It Works

1. **Function Definition:**
   - The Caesar Cipher is implemented as a function that takes three parameters: the text to be encrypted/decrypted, the shift amount, and the direction (encode or decode).
   - The function uses the shift amount to shift each letter in the text by a certain number of places in the alphabet.

2. **Encryption/Decryption Process:**
   - **Encoding:** Shift each letter in the input text forward by the shift amount to encrypt the message.
   - **Decoding:** Shift each letter in the input text backward by the shift amount to decrypt the message.

3. **Handling Edge Cases:**
   - The function handles wrapping around the alphabet (e.g., shifting 'z' by 1 results in 'a').
   - Non-alphabet characters remain unchanged.

4. **User Input:**
   - The program prompts the user to choose between encoding and decoding.
   - The user inputs the message and the shift amount.
   - The function is called with the appropriate parameters to perform the encryption or decryption.

5. **Output:**
   - The encrypted or decrypted text is displayed to the user.

### Key Concepts Learned

- **Function Parameters:** Passing multiple parameters to functions to control their behavior.
- **Conditionals:** Determining whether to encode or decode the text based on user input.
- **String Operations:** Manipulating strings by shifting characters.

## How to Run

1. Ensure Python is installed on your system.
2. Create a Python file for the Caesar Cipher.
3. Implement the logic as described in the explanations above.
4. Run the program by executing the Python file and follow the prompts to encode or decode a message.
