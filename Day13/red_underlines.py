# Lets fix the errors.

age = int(
    input("Age: "))  # In this line of code, the return is a string and not an integer. This is because we are trying to
# compare an integer with a string.
if age > 18:
    # print("You can drive a car.")
    print(f"You can drive a car at age {age}.")

# This shows up when I first run the program. IndentationError: expected an indented block after
# 'if' statement on line 4. Once fixed, it is not underlined anymore. We run the code:
# This new error shows up: TypeError: '>' not supported between instances of 'str' and 'int'.
# This is because we are trying to compare an integer with a string. We can't do that.
