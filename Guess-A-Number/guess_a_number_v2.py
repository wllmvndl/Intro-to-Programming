'''===-------------
# William Vandale #
#   Feb 18 2025   #
-------------==='''

# Imports

import math
import random
import time

def show_start_screen():
    pass

def show_end_screen():
    pass

def select_difficulty():
    selecting = True
    while selecting == True:
        difficulty = input("Select difficulty: ")
        difficulty = difficulty.lower()
        if difficulty in ["easy", "normal", "hard"]:
            selecting = False
        else:
            print("Select from Easy, Normal, or Hard.")
    print(difficulty.title() + " selected.")
    print()
    return difficulty
    
def play(difficulty):

    
    if difficulty == "easy":
        low = 1
        high = 10
        tries = math.ceil(math.log(high, 2)) + 1
    if difficulty == "normal":
        low = 1
        high = 100
        tries = math.ceil(math.log(high, 2)) + 1
    if difficulty == "hard":
        low = 1
        high = 1000
        tries = math.ceil(math.log(high, 2))

    number = random.randint(low, high)
    
    print(f"I'm thinking of a number from {low} to {high}...")
    print(f"You have {tries} attempts to guess it.")
    print("I bet you can't!")

    guess = -1
    while number != guess and tries > 0:
        guess = guess_input_validation()
        
        if guess > number:
            print("Too high!")
        if guess < number:
            print("Too low!")
        
        tries -= 1

        if number != guess:
            if tries > 1:
                print(f"{tries} attempts remaining.")
            elif tries == 1:
                print("1 attempt remaining")

    print()
    if number == guess:
        print("You got it!")
        print()
        if difficulty == "easy":
            print("Fine, but that's not a challenge...")
        if difficulty == "normal":
            print("Ok. I'm a little impressed.")
        if difficulty == "hard":
            print("No way! You cheated!")
    else:
        if difficulty != "easy":
            print("Haha! I knew you couldn't get it!")
        else:
            print("You lost on easy?!?!")
    print()

    return new_difficulty


def guess_input_validation():
    while True:
        try:
            guess = int(input("What is your guess? "))
            return guess
        except ValueError:
            pass


def raise_difficulty(difficulty):
    while True:
        again = input("Raise difficulty? ")
        again = again.lower()
        
        if again in ["y", "yes", "yeah"]:

            if difficulty == "normal":
                difficulty = "hard"
            else:
                difficulty = "normal"
            print(f"Changed difficulty to {difficulty}.")
            return False

    return difficulty

def lower_difficulty(difficulty):
    while True:
        again = input("Lower difficulty? ")
        again = again.lower()
        
        if again in ["y", "yes", "yeah"]:

            if difficulty == "hard":
                difficulty = "normal"
            else:
                difficulty = "easy"
            print(f"Changed difficulty to {difficulty}.")
            return difficulty
        
    return difficulty


def play_again():
    while True:
        again = input("Play again? ")
        again = again.lower()
        
        if again in ["y", "yes", "yeah"]:
            return True
        elif again in ["n", "no", "nah"]:
            return False
        else:
            print("I don't understand..")


def main():
    show_start_screen()
    difficulty = select_difficulty()
    new_difficulty = play(difficulty)
    
    running = True
    while running == True:
        running = play_again()
        print()
        play(new_difficulty)
        
    show_end_screen()

if __name__ == '__main__':
    main()
