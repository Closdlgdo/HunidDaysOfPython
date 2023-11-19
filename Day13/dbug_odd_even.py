# We will be debugging some more.

number = int(input())  # Which number do you want to check?

# if number % 2 = 0:
if number % 2 == 0:  # This is the correct way.
    print("This is an even number.")
else:
    print("This is an odd number.")

# This error message shows up when we run the code:
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
