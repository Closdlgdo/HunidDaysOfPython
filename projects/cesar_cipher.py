alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


# We create a new function called caesar() that accepts three parameters: a string, a shift amount, and a direction.
# The function should then apply the shift to each letter of the text, starting with the first letter and moving to the last letter
# in the alphabet. It should then return the new text.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")


should_end = False
while not should_end:
    print("Welcome to the Caesar Cipher Encoder/Decoder")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # What if the user enters a shift amount that is greater than the number of letters in the alphabet?
    # In that case, the program should ask the user to try again.
    shift = shift % 26
    print(f"Your shift amount is: {shift}")
# We call the caesar() function with the text, the shift, and the direction as parameters.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Thank you for using Caesar Cipher Encoder/Decoder. Goodbye")
########################
#
#
#
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
#
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
#
# else:
#     print("Invalid input")
