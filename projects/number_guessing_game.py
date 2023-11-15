# We are creating a number-guessing game that allows us to choose a difficulty level that would allow us
# a certain number of tries to guess the correct number.
# We will have a number from 1 to 100. Then the computer will ask for the user to choose a difficulty level.
# Easy level gives 10 tries. Hard level gives 5 tries.
import random

number = random.randint(1, 100)
easy_level = 10
hard_level = 5


def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return easy_level
    else:
        return hard_level


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {difficulty()} chances to guess the number.")
    guess = 0
    while guess != number:
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high. Guess again.")
        elif guess < number:
            print("Too low. Guess again.")
        else:
            print(f"You got it! The answer was {guess}.")


game()
