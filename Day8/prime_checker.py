# Create a function that checks whether the number is a prime number.
# Prime numbers are numbers that are only divisible by 1 and themselves.
# write code below this:
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input())
prime_checker(number=n)
