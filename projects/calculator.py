# 1. Let's create a calculator. We create functions for each of the operations.
# 2. We then want to store these functions inside a dictionary using the operations.
# 3. Let's create a for loop that iterates over the dictionary.
# 4. We then ask the user for the operation and the two numbers.
# 5. We then call the function corresponding to the operation.
# 6. We then print the result.

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():  # we will create a new function that calls itself. In programming, that is called recursion.
    num1 = float(input("What's the first number? "))

    for symbol in operations:  # when we use a for loop in the dictionary, it iterates over the keys rather than the values
        # or entries.
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
