def main():
    name = input("What is your name? ")
    print(hello(name))  # This version is a lot more testable.


def hello(to="world"):  # it is best practice to not have side effects if they are avoidable.
    return f"Hello {to}!"


if __name__ == "__main__":
    main()

# The assert statements that we are using are really designed to test arguments into functions and return values there from.
