# We are creating a number-guessing game that allows us to choose a difficulty level that would allow us
# a certain number of tries to guess the correct number.
# We will have a number from 1 to 100. Then the computer will ask for the user to choose a difficulty level.
# Easy level gives 10 tries. Hard level gives 5 tries.
from random import randint

easy_level = 10
hard_level = 5

turns = 0


def game(guess, number, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > number:
        print("Too high.")
        return turns - 1
    elif guess < number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {guess}.")


def difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return easy_level
    else:
        return hard_level


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)

    turns = difficulty()

    guess = 0
    while guess != number:
        print(f"You have {turns} chances to guess the number.")

        guess = int(input("Make a guess: "))

        turns = game(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


main()
