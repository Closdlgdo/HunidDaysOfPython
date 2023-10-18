# # Libraries are files of code that other have written and can be used with others.
# # Modules are libraries that have one or more functions.
# # statistics library is a module in Python. It is used to calculate means medians modes or aspects of datasets.
# # Import is a module in Python. It is used to import other modules.
import statistics

#
# Problem 1: Mean: The mean is the average of a set of numbers. To calculate the mean, you add up all the numbers and
# then divide by the total count of numbers.
# Write a program that calculates and prints the mean of a list of numbers.
#
print(statistics.mean([100, 90, 80, 95, 99, 70]))  # mean is one of the functions of the statistics module.

# Problem 2: Median: the middle value of a set of numbers when they are arranged in ascending order. If the set has an even
# number of values, the median is the average of the two middle values.
# Write a program that calculates and prints the median of a list of numbers.
#
print(statistics.median([100, 90, 80, 80]))

# Problem 3: Mode: the value that occurs most frequently in a set of data. A set can have one mode, more than one mode, or no mode at all.
# Write a program that calculates and prints the mode of a list of numbers.
#
print(statistics.mode([100, 90, 80, 95, 99, 70]))

# Problem 4: Range: the difference between the largest and smallest values in a set of numbers. It gives an idea of the
# spread or dispersion of the data.
# Write a program that calculates and prints the range of a list of numbers.
#

print(statistics.pstdev([100, 90, 80, 95, 99, 70]))

# Problem 5: Standard Deviation: measures the amount of variation or dispersion in a set of values. A lower standard deviation
# indicates that the values tend to be closer to the mean, while a higher standard deviation indicates greater variability.
# Write a program that calculates and prints the standard deviation of a list of numbers.
#
print(statistics.stdev([100, 90, 80, 95, 99, 70]))

# Problem 6: Variance: another measure of the spread of data points. It is the average of the squared differences from the Mean.
# Write a program that calculates and prints the variance of a list of numbers.
#

print(statistics.variance([100, 90, 80, 95, 99, 70]))

# Problem 7: Harmonic Mean: measure of central tendency that is especially useful for numbers that are rates or ratios.
# It is the reciprocal of the arithmetic mean of the reciprocals.
# Write a program that calculates and prints the harmonic mean of a list of numbers.
#

print(statistics.harmonic_mean([100, 90, 80, 95, 99, 70]))

# Problem 8: Geometric Mean: the average of a set of numbers, calculated by multiplying the numbers together and then
# taking the nth root (where n is the total count of numbers).
# Write a program that calculates and prints the geometric mean of a list of positive numbers.
#

print(statistics.geometric_mean([100, 90, 80, 95, 99, 70]))

# Problem 9: Midrange: the average of the maximum and minimum values in a data set. It provides a rough measure of the
# center of the data.
# Write a program that calculates and prints the midrange (the average of the maximum and minimum values) of a list of numbers.
#
data = [100, 90, 80, 95, 99, 70]
midrange = (max(data) + min(data)) / 2
print(midrange)
# For each problem, you can use the appropriate function from the statistics module to perform the calculation.
#
