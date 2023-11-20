# Debugging is the process of removing errors from the code.
# If the problem is messy and not well understood, untangle the problem to better understand it.

# Describing the problem:
def my_function():
    for i in range(1, 20):  # This print function will never print because the range will never reach 20.
        # the range returns an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
        # So the range for this function will only go from 1 (inclusive) to 19 since the 20 is (exclusive).
        if i == 20:
            print("You got it")


my_function()
