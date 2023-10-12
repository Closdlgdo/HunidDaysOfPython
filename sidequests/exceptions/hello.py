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

# python error handling also allows else.

try:
    x = int(input("Whats x? "))

except ValueError:
    print('x is not a integer')
else:
    print(f'x is {x}')
