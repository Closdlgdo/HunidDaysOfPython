# Libraries are files of code that other have written and can be used with others.
# Modules are libraries that have one or more functions.
# Random library is a module in Python. It is used to generate random numbers.
# Import is a module in Python. It is used to import other modules.
# random.choice(seq) = the parameter of random.choice is seq which means sequence. It is a list or list-like.
# e.g.
# heads or tails
# import random  # we are technically importing everything from the random library.
#
# coin = random.choice(["heads", "tails"])  # here we have to type .choice because we are using the full random library,
# so we have to specify the function (.choice).
# print(coin)

# from keyword is used to import a function from a module.
from random import choice

color = choice(["red", "blue", "yellow"]).capitalize()
name = choice(["carlos", "theano", "lucas"]).capitalize()
pokemon = choice(["pikachu", "charmander", "squirtle", "bulbasaur"]).capitalize()

print(f"Your starting color is {color}.\nYour name is {name}.\nYour favorite Pokemon is {pokemon}")
