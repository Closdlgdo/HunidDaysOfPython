# Randomisation like tetris or any game really.
# Python uses the mersenne twister algorithm.
#
# import random
#
# random_integer = random.randint(1, 100)
# print(random_integer)
#
# random_float = random.random()
# print(random_float * 5)

import random

random_integer = random.randint(0, 1)

if random_integer == 0:
    print("Heads")
else:
    print("Tails")
