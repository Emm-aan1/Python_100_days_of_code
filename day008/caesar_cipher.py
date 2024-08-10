alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(txt, shift_txt, direct):
    cipher_text = ""

    for char in txt:
        position = alphabets.index(char)
        if direct == "encode":
            new_pos = position + shift_txt
        elif direct == "decode":
            new_pos = position - shift_txt
        new_pos %= len(alphabets)
        cipher_text += alphabets[new_pos]

    return cipher_text


result = caesar(text, shift, direction)

if direction:
    print(f"Here is the {direction}d result: {result}")
