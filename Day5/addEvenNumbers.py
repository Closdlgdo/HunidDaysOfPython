# write a program that calculates the sum of all the even numbers from 1 to X. If X is 100
# then the first even number would be 2 and the last one is 100: i.e. 2 + 4 + 6 + ... + 98 + 100.
# There should only be 1 print statement in your console output. It should just print the
# final total and not every step of the calculation.

target = int(input())  # number between 0 and 1000
even_sum = 0
for i in range(2, target + 1):
    if i % 2 == 0:
        even_sum += i
print(even_sum)
