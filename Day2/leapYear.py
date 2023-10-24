input_year = int(input("Which year do you want to check? "))


def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False
