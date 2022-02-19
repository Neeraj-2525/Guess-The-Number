# Name == Neeraj
# Objective: To make a game which says to guess a number and take it as a input from user

import random

n = random.randint(1, 50)  # n : Number which should be guessed by the user

choice = 'y'
while choice.lower() == 'y':
    number_of_guesses = 1
    print("__________________LET'S PLAY - GUESS THE NUMBER__________________")
    print("                       (Developer-Neeraj)\n\n")
    print("How to play: Guess the number between 1-50 with some given hints, use your num-pad to type")
    print("(YOU GOT 6 CHANCES TO GUESS THE NUMBER)")

    while number_of_guesses <= 6:
        guess_number = int(input("Guess the number: "))

        if guess_number < n:
            print("wrong!\nHint: you have entered a smaller number\n")

        elif guess_number > n:
            print("wrong!\nHint: you have entered a greater number\n")

        else:
            print("####You___won####")
            print("you took", number_of_guesses, "chances to finish")

            break

        print("(No. of guesses left:", 6 - number_of_guesses, ")")
        number_of_guesses += 1

    if number_of_guesses > 6:
        print("You Lose 🙁")
        print("GAME___OVER")

    choice = input("DO YOU WANT TO PLAY AGAIN Y/N ?")
    print("Thank You for playing!")