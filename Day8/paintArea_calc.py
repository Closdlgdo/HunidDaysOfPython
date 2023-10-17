# You are painting a wall. The instructions on the paint can say that 1 can of paint
# can cover 5 square meters of the wall. Given a random height and width of the wall, calculate
# how many cans of paint you’ll need to buy.
import math


# number of cans = (wall height * wall width) / coverage per can.
# Write code here:
def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil((height * width) / cover)} cans of paint.")


test_h = int(input())  # height of wall (m)
test_w = int(input())  # width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
