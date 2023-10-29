def greetings(name):
    print(
        f"Hello {name}!")  # We cannot reuse this function in other scenarios because it only prints out to the console.

    # ^^^ Functions that perform a task. ^^^ Printing something on the terminal.
    # Functions that return a value. A function like round(1.9) will return 2.
    # We will rewrite this function to return a value in the second form rather than the first.


def get_greeting(name):  # we add the name parameter to the function.
    return f"Hello {name}!"  # we return this formatted string.


#  this second form is not tied to the terminal and returns a value to anything we want.


message = get_greeting("Carlos")  # because it returns a value, we can store that value in a variable.
print(message)
