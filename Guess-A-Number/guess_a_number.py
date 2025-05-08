'''===-------------
# William Vandale #
#   Feb 14 2025   #
-------------==='''

# Imports

import random
import time

# Functions

def show_start_screen():
    pass


def show_end_screen():
    pass


def play():
    low = 1
    high = 10
    tries = 3

    
    number = random.randint(low, high)
    #print(number)
    
    print(f"I'm thinking of a number from {low} to {high}...")
    print("Can you guess what it is? ")
    print()
    
    guess = -1

    while guess != number and tries > 0:

        guess = input("Guess! ")
        guess = int(guess)
        
        if guess > number:
            print("That's a little too high...")
        elif guess < number:
            print("That's a little too low...")
        tries -= 1

    print()
    if guess == number:
        print("You win!")
    else:
        print("You lost...")


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
    
# Play Game

def main():
    show_start_screen()

    running = True
    
    while running == True:
        play()
        running = play_again()
        print()
        
    show_end_screen()

if __name__ == '__main__':
    main()
