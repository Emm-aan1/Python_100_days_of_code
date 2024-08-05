import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ease_pass = ''
for char in range(1, nr_letters + 1):
    rand_char = random.choice(letters)
    ease_pass += rand_char

for sym in range(1, nr_symbols + 1):
    rand_sym = random.choice(symbols)
    ease_pass += rand_sym

for num in range(1, nr_numbers + 1):
    rand_num = random.choice(numbers)
    ease_pass += rand_num
print(ease_pass)


hard_pass = []
password = ''
for char in range(1, nr_letters + 1):
    rand_char = random.choice(letters)
    hard_pass.append(rand_char)

for sym in range(1, nr_symbols + 1):
    rand_sym = random.choice(symbols)
    hard_pass.append(rand_sym)

for num in range(1, nr_numbers + 1):
    rand_num = random.choice(numbers)
    hard_pass.append(rand_num)

# print(hard_pass)
random.shuffle(hard_pass)
for char in hard_pass:
    password += char

print(password)
