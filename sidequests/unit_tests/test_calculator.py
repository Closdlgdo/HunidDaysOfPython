# The sole purpose of this file is to test the calculator.py file's square function.

from calculator import square  # import square function from calculator.py file


def main():  # in order to call the function, the sole purpose of main is to test test_square.
    test_square()


def test_square():  # a convention for square functions
    if square(2) != 4:
        print("test failed")
    if square(3) != 9:
        print("test failed")


# these tests are meant to run automatically instead of having to manually run them.


if __name__ == "__main__":  # boilerplate to kick off a process.
    main()  # call the main function and adding the conditional argument, by conditionally calling main() just in case
    # we import anything from this file, elsewhere.
    # no output prints out.
