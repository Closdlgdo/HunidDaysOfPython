# write a program that calculates the sum of all the even numbers from 1 to X. If X is 100
# then the first even number would be 2 and the last one is 100: i.e. 2 + 4 + 6 + ... + 98 + 100.
# There should only be 1 print statement in your console output. It should just print the
# final total and not every step of the calculation.

target = int(input())  # number between 0 and 1000
even_sum = 0
for i in range(2, target + 1):
    if i % 2 == 0:
        even_sum += i
print(even_sum)

#
# 1. target = int(input()):
# This line prompts the user to input a number (presumably between 0 and 1000).
# int(input()) takes a user input as a string and converts it to an integer using int(). The result is then assigned to the variable target.
# 2. even_sum = 0:
# This initializes a variable even_sum to 0. This variable will be used to keep track of the sum of even numbers.
# 3. for i in range(2, target + 1)::
# This is a for loop that iterates over a range of numbers from 2 to target (inclusive).
# range(2, target + 1) generates a sequence of numbers starting from 2 up to and including the value of target.
# 4. if i % 2 == 0::
# Within the loop, this checks if i is even. The % operator gives the remainder of a division. If i is even, i % 2 will be 0.
# 5. even_sum += i:
# If i is even, it adds i to the even_sum. This accumulates the sum of all even numbers encountered during the loop.
# 6. print(even_sum):
# After the loop completes, this prints the final value of even_sum, which represents the sum of all even numbers between 2 and target.
#
# Here's an example to illustrate the code's execution:
#
# If the user inputs 10 as target, the code will:
# Initialize even_sum as 0.
# Start a loop from 2 to 10.
# For each i in this range, if i is even, it adds i to even_sum.
# After the loop, it prints the value of even_sum, which will be 2 + 4 + 6 + 8 + 10 = 30.
