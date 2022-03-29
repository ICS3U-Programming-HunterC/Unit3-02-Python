#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 28, 2022
# This is a program for a user to guess the correct number


import constants


def main():
    # this function checks if the guess is correct

    # get the user's guess
    guess = float(input("Enter a number between 1 and 9: "))
    print("")

    # check if the user's guess is correct or incorrect
    if guess != constants.CORRECT_NUMBER:
        print("That is wrong!")

    if guess == constants.CORRECT_NUMBER:
        print("That is correct!")


if __name__ == "__main__":
    main()
