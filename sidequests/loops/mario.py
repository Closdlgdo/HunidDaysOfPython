# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")
#

def main():
    print_square(3)


#     # print_column(3)
#     print_row(4)
#
# # # This code defines a function called print_column that takes a parameter height. It prints a column of # characters,
# # # with the number of rows equal to the height value. The commented line after the loop is an alternative way to achieve the same result using string multiplication and the end parameter of the print function.
# # def print_column(height):
# #     for _ in range(height):
# #         print("#")
# #     #  we can also do this to get the same: print("#\n" * height, end="")
#
#
# def print_row(width):
#     print("?" * width)


def print_square(size):
    # For each row in square
    for i in range(size):
        print("# " * size)
        # # For each brick in row
        # for j in range(size):  # nesting loops
        #
        #     # print bricks
        #     print("#", end="")
        #
        # print()  # this is basically the \n.


main()
