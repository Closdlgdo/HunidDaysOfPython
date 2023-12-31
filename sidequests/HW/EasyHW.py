# Exercise 1: Simple Math Operations
# Write a Python program that:
#
# Takes two numbers as input from the user.
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# # Calculates and prints their sum, difference, product, and quotient.
# summation = x + y
# difference = x - y
# product = x * y
# quotient = x / y
#
# print("Sum:", summation, "Difference:", difference, "Product:", product, "Quotient:", quotient)

# Exercise 2: Factorial Calculator
# Write a Python function that calculates the factorial of a given number.
# factorial = int(input("Enter a number: "))
# result = 1  # This variable will be used to keep track of the current factorial.
# for i in range(1,
#                factorial + 1):  # This line starts a loop that will iterate over a range of numbers from 1 to factorial + 1.
#     # i will take on each of these values in turn.
#     result *= i  # Inside the loop, this line multiplies result by the current value of i.
#     # This is the step where the factorial is being calculated.
#     print("Factorial: ", result)
#
# #
# #

# Exercise 3: Guess the Number Game
# Write a program that generates a random number between 1 and 100. The user should guess the number. Provide hints like
# "Too high" or "Too low" until they guess correctly.

import random

desired_number = random.randint(1, 100)  # This generates a random number between 1 and 100.

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < desired_number:
        print("Too low")
    elif guess > desired_number:
        print("Too high")
    else:
        print("You guessed it correctly!")
        break


# Exercise 4: Fibonacci Sequence
# Write a Python function that generates the first n numbers in the Fibonacci sequence.
#
#

# Exercise 5: String Reversal
# Write a function that takes a string as input and returns the reverse of the string.
#
#

# Exercise 6: Prime Number Checker
# Write a function that checks if a given number is prime or not.
#
#

# Exercise 7: List Manipulation
# Write a program that:
#
# Creates a list of numbers.
# Removes the duplicates.
# Finds the maximum and minimum values.
# Sorts the list in ascending order.
#
#

# Exercise 8: Palindrome Checker
# Write a function that checks if a given word or phrase is a palindrome.
#
#

# Exercise 9: Rock, Paper, Scissors Game
# Write a Python program that allows the user to play a game of Rock, Paper, Scissors against the computer.
#
#

# Exercise 10: File Handling
# Write a program that reads a text file, counts the frequency of each word, and prints the top 5 most frequent words.
