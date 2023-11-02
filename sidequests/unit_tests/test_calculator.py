# # The sole purpose of this file is to test the calculator.py file's square function.
# # Pytest is a third party test framework for Python. It will automate the testing of your code as long as you write the code.
# from calculator import square  # import square function from calculator.py file
#
# We will reintroduce the error so we can run all the tests and see which will fail.
from calculator import square


# We will separate our test code into multiple tests.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

# def main():  # in order to call the function, the sole purpose of main is to test test_square.
#     test_square()
#
#
# # Assert: the assert statement is used to check if a given condition is true. If the condition is false, an
# # AssertionError is raised. Assert is commonly used in unit tests to verify that certain assumptions about the code are true.
#
#
# def test_square():  # a convention for square functions
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("square(2) is not equal to 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("square(3) is not equal to 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("square(-2) is not equal to 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("square(-3) is not equal to 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("square(0) is not equal to 0")
#
#
# # This particular test is meant to test the square function.
# # these tests are meant to run automatically instead of having to manually run them.
#
#
# if __name__ == "__main__":  # boilerplate to kick off a process.
#     main()  # call the main function and adding the conditional argument, by conditionally calling main() just in case
#     # we import anything from this file, elsewhere.
#     # no output prints out.
