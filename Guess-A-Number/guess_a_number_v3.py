'''===-------------
# William Vandale #
#   Feb 20 2025   #
-------------==='''

### Guess-a-Number Console Game

import math
import random
import time

###

def show_start_screen():
    print('''    __________________________          ''')
    print('''   |   ___________________     |___     ''')
    print('''   |  ||                  |    |   |    ''')
    print('''   |  ||  Guess-a-Number  |    |   \\   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||  >Press any Key  |    |   ||   ''')
    print('''   |  ||  >Press any Key  |    |   ||   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||  Guess-a-Number  |    | □ ||   ''')
    print('''   |  ||__________________|    | □ ||   ''')
    print('''   |_□_______________________|_□_||     ''')
    print('''      _______|__________|_|||||____    ''')
    print('''     |_________________________|_|||   ''')
    input()


def show_end_screen():
    print('''    __________________________          ''')
    print('''   |   ___________________     |___     ''')
    print('''   |  ||                  |    |   |    ''')
    print('''   |  ||  Guess-a-Number  |    |   \\   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||    Thanks for    |    |   ||   ''')
    print('''   |  ||     Playing!     |    |   ||   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||  Guess-a-Number  |    | □ ||   ''')
    print('''   |  ||__________________|    | □ ||   ''')
    print('''   |_□_______________________|_□_||     ''')
    print('''      _______|__________|_|||||____    ''')
    print('''     |_________________________|_|||   ''')
    print()
    print("2025. Game and Art Created by William Vandale.")
    
###

def greet_user():
    print("Beat ConviBot in Guess-a-Number!")
    time.sleep(0.2)
    print("Booting...")
    time.sleep(0.2)
    print("Hello! I'm ConviBot!")
    name = input("What's your name? ")
    name = same_name(name.lower())
    print(f"Nice to meet you {name}!")
    print("But I'm not here to chat today...")
    print("I am going to WIN!!!")
    return name


def same_name(name):
    # Tests if the inputted name is also ConviBot
    if "convibot" in name:
        print("No it isn't! I'm ConviBot! We can't both be named ConviBot!")
        name = input("Tell me your real name. ")
        # Iteration 1
        if "convibot" in name.lower():
            name = input("I said your REAL name. No one else is named ConviBot. ")
        # Iteration 2
        if "convibot" in name.lower():
            name = input("YOUR NAME! NOT MINE! YOURS! WHAT IS IT??? ")
        # Iteration 3
        if "convibot" in name.lower():
            print("Fine then. I will just call you annoying.")
            name = "Annoying User"
    name = str.title(name)
    return name

###

def change_difficulty(won_game, difficulty):
    if difficulty == "initialize":
        new_difficulty = select_difficulty() # first pass
    else:
        if won_game == True and difficulty in ["normal", "easy"]:
            new_difficulty = raise_difficulty(difficulty)
        elif won_game == False and difficulty in ["hard", "normal"]:
            new_difficulty = lower_difficulty(difficulty)
        else:
            new_difficulty = difficulty
    return new_difficulty


def select_difficulty():
    selecting = True
    while selecting == True:
        difficulty = input("But first select a difficulty: ")
        difficulty = difficulty.lower()
        if difficulty in ["easy", "normal", "hard"]:
            selecting = False
        else:
            print("Select from Easy, Normal, or Hard.")
    #print(difficulty.title() + " selected.")
    print()
    return difficulty


def raise_difficulty(difficulty):
    changing = True
    
    while changing == True:
        answer = input("Raise difficulty? ")
        answer = answer.lower()

        if answer in ["y", "yes", "yeah"]:
            changing = False
            if difficulty == "normal":
                new_difficulty = "hard"
                print("Raised difficulty to Hard")
            elif difficulty == "easy":
                new_difficulty = "normal"
                print("Raised difficulty to Normal")
            
        elif answer in ["n", "no", "nah"]:
            new_difficulty = difficulty
            changing = False

        else:
            pass # invalid input
    print()        
    return new_difficulty


def lower_difficulty(difficulty):
    changing = True
    
    while changing == True:
        answer = input("Lower difficulty? ")
        answer = answer.lower()

        if answer in ["y", "yes", "yeah"]:
            changing = False
            if difficulty == "hard":
                new_difficulty = "normal"
                print("Lowered difficulty to Normal")
            elif difficulty == "normal":
                new_difficulty = "easy"
                print("Lowered difficulty to Easy.")
            
        elif answer in ["n", "no", "nah"]:
            new_difficulty = difficulty
            changing = False

        else:
            pass # invalid input
    print()       
    return new_difficulty

###

def play(difficulty, name):
    # Difficulty Settings

    print("Difficulty: " + difficulty.title())
    
    lower_bound = 1
    if difficulty == "easy":
        upper_bound = 10
        tries = math.ceil(math.log(upper_bound, 2)) + 1
    if difficulty == "normal":
        upper_bound = 100
        tries = math.ceil(math.log(upper_bound, 2)) + 1
    if difficulty == "hard":
        upper_bound = 1000
        tries = math.ceil(math.log(upper_bound, 2))

    number = random.randint(lower_bound, upper_bound) # What the bot is thinking of
    print(f"I'm thinking of a number from {lower_bound} to {upper_bound}...")
    print(f"You have {tries} attempts to guess it.")
    print("I bet you can't!")
    
    won_game = start_guessing(number, tries)
    round_complete_screen(won_game, difficulty, number, name)
    return won_game


def start_guessing(number, tries):
    guess = -1 # initialization
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
        won_game = True
    else:
        won_game = False
    return won_game


def round_complete_screen(won_game, difficulty, number, name):
    if won_game == True:
        print("You got it!")
        print()
        if difficulty == "easy":
            print(f"Fine {name} you win, but that's not a challenge...")
        if difficulty == "normal":
            print(f"Ok, {name}. I'm a little impressed.")
        if difficulty == "hard":
            print("No way! You cheated!")
    else:
        if difficulty != "easy":
            print(f"Haha! I knew you couldn't get it, {name}!")
        else:
            print("You lost on easy?!?!")
        print(f"The number I was thinking of was {number}.")
    print()

###

def guess_input_validation():
    while True:
        try:
            guess = int(input("What is your guess? "))
            return guess
        except ValueError:
            pass

###

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

###
        
def main():
    
    show_start_screen()
    name = greet_user()

    won_game = False
    difficulty = "initialize"
    playing = True
    
    while playing == True:
        difficulty = change_difficulty(won_game, difficulty)
        won_game = play(difficulty, name)
        playing = play_again()

    show_end_screen()
        
if __name__ == '__main__':
    main()
