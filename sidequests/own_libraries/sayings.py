def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello {name}!")


def goodbye(name):
    print(f"Goodbye {name}!")


main()  # it seems that what we want to print int the say.py file is not properly printing because we are blindly
# calling the function main(). Main() gets called no matter what.
