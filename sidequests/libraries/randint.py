# random.randint(a, b) = get back a random integer between a and b inclusive.
import random

# Problem: Dice Roll Simulator
# Write a program that simulates rolling a six-sided die. The program should generate a random number between 1 and 6
# and print the result.
number = random.randint(1, 6)
print(f"You rolled a {number}")

# Write a program that generates a random number within a user-specified range. The program should prompt the user for
# a minimum and maximum value, and then generate a random number between those two values (inclusive).
min_val = int(input("Enter a minimum value: "))
max_val = int(input("Enter a maximum value: "))
final_val = random.randint(min_val, max_val)

print(f"Your random number is: {final_val}")
