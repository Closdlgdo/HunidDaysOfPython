# random.shuffle(x) = shuffle the list x. Makes the list into a random order.
import random

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
