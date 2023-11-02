def main():
    x = input('What is x? ')  # Let's assume someone forgets to convert the input to an int.
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == '__main__':  # Let's get into the habit of making sure main() is not always called. This is a good habit
    # to get into. This is incase I want to import this file into another file, we don't want to call main() automatically.
    main()
