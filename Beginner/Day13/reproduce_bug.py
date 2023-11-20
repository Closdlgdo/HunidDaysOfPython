# Reproduce the bug:
from random import randint

#
# dices_imgs = ["1", "2", "3", "4", "5", "6"]
# dices_num = randint(1, 7)
#
# print(dices_imgs[dices_num])

# The error being produced here is the IndexError: list index out of range.
# The reason behind this is that the randint function is starting it at 1 (inclusive).
# fixed:

dices_imgs = ["1", "2", "3", "4", "5", "6"]
dices_num = randint(0, 5)  # Fix the bug by changing the range of randint to start at 0 (inclusive) instead of 1.
print(dices_imgs[dices_num])
