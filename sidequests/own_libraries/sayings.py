def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello {name}!")


def goodbye(name):
    print(f"Goodbye {name}!")


if __name__ == "__main__":
    main()  # it seems that what we want to print int the say.py file is not properly printing because we are blindly
# calling the function main(). Main() gets called no matter what.
# __name__ is a variable that is set to the name "main" of the current module when ran in the command line.
