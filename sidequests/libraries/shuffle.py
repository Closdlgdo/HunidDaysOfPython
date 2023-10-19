# random.shuffle(x) = shuffle the list x. Makes the list into a random order.
import random

# Random Card shuffle that prints out the four names randomly.
cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

# Randomizing the list of artists' order.
artist = ["J. Cole", "Kendrick Lamar", "Drake"]
random.shuffle(artist)
for artist in artist:
    print(artist)


# a program that takes a word from the user, shuffles the letters, and prints the resulting scrambled word.
def scrambles(word):
    # Convert the word into a list of letters
    letters = list(word)

    # Shuffle the letters
    random.shuffle(letters)

    # Convert the shuffled letters back into a string
    scramble = ''.join(letters)

    return scramble

    # Get input from the user


word = input("Enter a word: ")

# Call the function to scramble the word
scrambled_word = scrambles(word)

# Print the scrambled word
print(f"Scrambled word: {scrambled_word}")
