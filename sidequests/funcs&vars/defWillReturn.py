def main():  # we want to square the value of x.
    x = int(input("What is x? "))
    print("x squared is,", square(x))


def square(n):
    return n * n
    # The return statement is used to specify the value that the function should return when it is called.
    # In this case, the function is expected to return the square of the input value n multiplied by itself (n * n).
    # The returned value can be used in other parts of the code or assigned to a variable.
    # return n ** 2 means raises the thing in the left to the power of the right
    # there is also a function called pow that raises something to the power and takes in two arguments
    # return pow(n, 2)


main()
