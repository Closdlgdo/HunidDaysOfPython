# print('hello world)
#       # print('hello world)
# #           ^
# # SyntaxError: unterminated string literal (detected at line 1)
# # A syntax error is when you have a user error in your code, meaning you could've written something wrong and that causes
# # your program to not run.

# Let's play with some numbers to see a Runtime error.

# x = int(input("Whats x? "))
# print(f'x is {x}')

# x = int(input("Whats x? "))
# ValueError: invalid literal for int() with base 10: 'cat'
# try:
#     x = int(input("Whats x? "))
#     print(f'x is {x}')
# except ValueError:
#     print('x is not a integer')

# We want to write our code with error handling in mind. Program defensively.
# Imagine you're playing a game, and you want to catch a ball that your friend throws to you. Sometimes you might catch
# the ball smoothly, but other times you might miss or drop it.
#
# In programming, the try and except statements work similarly. When you have a piece of code that might cause an error
# or "throw an exception", you can put that code inside a try block. It's like trying to catch the ball.
#
# If an error occurs inside the try block, instead of the program crashing and stopping, the code inside the except block
# will run. It's like having a backup plan in case you miss catching the ball. The except block helps you handle or deal
# with the error gracefully.
#
# So, using try and except helps you write code that can handle errors or unexpected situations without crashing the
# entire program. It allows you to continue running the program and take appropriate actions when something goes wrong.

# try:
#     x = int(input("Whats x? "))
#
# except ValueError:
#     print('x is not a integer')
#
# print(f'x is {x}')
#
# # print(f'x is {x}')
# # NameError: name 'x' is not defined

# # python error handling also allows else.
#
# try:
#     x = int(input("Whats x? "))
#
# except ValueError:
#     print('x is not a integer')
# else:
#     print(f'x is {x}')

# # We will now use a loop to continue prompting the user for the correct input incase they don't input what we want.
# while True:
#     try:
#         x = int(input("Whats x? "))
#     except ValueError:
#         print('x is not a integer')
#     else:
#         break
#
# print(f'x is {x}')

# If we want to get user input on the daily or often, we can create a function that can be used by others as well.
# This code defines a function called main that does the following:
#
# Calls a function called get_int() which returns an integer value.
# Stores the returned integer value in a variable called x.
# Prints the value of x using f-string formatting.
def main():
    x = get_int("What's x? ")
    print(f'x is: {x}')


# This code defines a function called get_int() that repeatedly asks the user for input until they provide a valid integer.
# It uses a while loop and a try-except block to handle any ValueError that may occur if the user enters a non-integer
# value. Once a valid integer is provided, the function breaks out of the loop and returns the value.


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # return can break you out of a loop and return a value. Stronger and more useful thank Break.
        except ValueError:
            pass  # the pass statement is a placeholder that does nothing. It is used when a statement is syntactically
            # required but you do not want to perform any action at that point in your code.


main()
