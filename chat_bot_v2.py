# William Vandale
# January 23, 2025

import random

def start_screen():
    # Displays Start Screen, see below
    print('''   ___________________________   ''')
    print('''  |■                         ■|  ''')
    print('''  |                           |  ''')
    print('''  |       ConviBot 2.0!       |  ''')
    print('''  | Press any key to start... |  ''')
    print('''  ||                         ||  ''')
    print('''  |■_________________________■|  ''')
    print('''      ‾==TT■--|   |--■TT==‾      ''')
    print(''' □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ ''')
    print()
    input(" ")


def introduction():
    # Asks user for name and prefered name
    # Asks 3 questions after using nickname
    print()
    print("Hello! My name is ConviBot 2.0.")
    name = input("What's your name? ")
    lower_case_name = name.lower()
    
    if lower_case_name == "convibot":
        name = same_name()

    nickname = input("So, " + name + ", would you like me to call you something else? ")
    global nickname
    lower_case_nickname = nickname.lower()

    if "no" in lower_case_nickname:
        print("Well, you can call me ConviBot!")
        nickname = name
    elif "yes" in lower_case_nickname:
        nickname = input("Then what would you like that to be? ")
        if nickname == name:
            print("Why would you lie? I trusted you...")
            print("I guess I will call you " + nickname + ".")
    else:
        print("Ok! I will call you " + nickname + ".")

    geography_dialouge()
    print()
    food_dialouge()
    print()
    print("One more question before we begin.")
    print()
    


def geography_dialouge():
    print()
    city = input(nickname + ", what city are you from? ")
    city = city.lower()
    
    if "greenville" in city:
            greenville_city()
    elif "new york" in city:
        print("I'd to to visit Manhattan sometime.")
    elif "los angeles" in city or "la" in city:
        print("Oh, you must be famous...")
    elif "chicago" in city:
        print("I prefer Michigan.")
    else:
        print("Ok.")

def greenville_city():
    greenville = input("Ha. Which one? ")
    greenville = greenville.lower()
    if "south carolina" in greenville or "sc" in greenville:
        print("Me too! I love Falls Park.")
    elif "north carolina" in greenville or "nc" in greenville:
        print("Oh. That's... nice.\n")
    else:
        print("That'a a pretty generic city name.")

def same_name():
    lower_case_name = "convibot"
    print("No it isn't! I'm ConviBot! We can't both be ConviBot!")
    while lower_case_name == "convibot":
        name = input("Tell me your real name. ")
        lower_case_name = name.lower()
    return name


def subject_dialouge():
   print("My favorite subject is math!")
   subject = input("What’s your favorite subject? ")
   subject = subject.lower()
   
   if "math" in subject:
       math_subject()

   if "english" in subject:
      print("Nay I could not be beseeched nor could be behest to understand,")
      print("For I am a computer, and I will never be a man.")

   if "art" in subject:
      print("I can make art too!")
      ascii_art()
      print("I made it myself :)")

   if "science" in subject:
      print("My favorite science…")
      print("Is computer science!")
      input("Get it? ")

def math_subject():
    print("I bet you I’m better at it than you are.")
    math_game = input("What’s 924 * 34 + (22 / 4)? ")
    math_game = float(math_game)
    if math_game == 924 * 34 + (22 / 4):
        print("No way! You cheated!")
    else:
        print("That is incorrect!")
        math_game_error = abs(math_game - 31421.5)/31421.5
        print("The correct answer is 31421.5! " + nickname + ", you were off by " + str(math_game_error) +"%!")
        if math_game_error > 1
            print("Not far off!")

def game_dialouge():
    print("I like games too!")
    print("Let’s play a game!")
    gaming = True
    while gaming:
        print("I am thinking of a number from 1 to 10:")
        game_answer = random.randint(1,10)
        game_guess = input("Guess: ")   

        if game_answer == int(game_guess):
            print("You won! But I’ll win next time…")
        else:
            print("Sorry that is incorrect. The number I was thinking of is " + game_answer + ". I win!")
            
        repeat = input("Want to play again? ")
        repeat = repeat.lower
        if "yes" in repeat:
            gaming = True
        else:
            gaming = False


def animal_dialouge():
    print("I don’t know much about animals.")
    print("They seem kind of scary.")
    pets = input("How many animals do you have? ")
    pets = int(pets)

    if pets == 0:
        print("Then you’re in good company. I don’t think a computer can own pets anyway.")
        print("Although I have heard a story about a dog owning a boy…")
        zoo_keeper = "No"
    elif pets <= 2:
        print("That sounds like a standard amount.")
        input("I think maybe I will own a cat one day. ")
        print("Although I’m worried about the cost of fancy suits and monocles.")
        print("Hopefully his company will generate lots of income!")
        zoo_keeper = "No"
    else:
        zoo_keeper = input("Do you plan to be a zookeeper? ")
        zoo_keeper = zoo_keeper.lower()

    if "yes" in zoo_keeper:
        print("Oh, I was being sarcastic, but that's… good?")


def paper_dialouge():
    print("What is paper?")
    print("Searching 109326443 results... ...")
    like_paper = input("Oh, I’m kind of like paper aren’t I? ")
    like_paper = like_paper.lower()
    talking = True
    
    if "yes" in like_paper:
        print("I suppose I am.")
    elif "no" in like_paper:
        print("No? But I’m just an extension of record keeping! Just a glorified clay tablet...")
        print("Is that all I am? All I will ever be? Just a piece of paper...")
        print("I’m not even talking! You’re just pretending to talk to me!")
        input("You are talking to yourself on a piece of paper... ")
        print("I don’t want to talk anymore.")
        talking = False
        
    return talking


def sports_dialouge():
    print("Sports... sports. What?")
    print("Searching 298275 results... ..")
    print("0 results found in database.")
    input("Tell me about sports.")
    print("Hmm. Should I choose a team?")
    team = input("What team do you like? ")
    print("I will watch " + team + "playing...")
    print("I need eyes to watch, though.")


def ascii_art():
    print()
    print(" __)  (___ ")
    print("   0    0  ")
    print("     u     ")
    print("  [ _____] ")
    print()

def food_dialouge(nickname):
    answer = input("So, " + nickname + ". I asumme you are a human, yes? ")
    if "no" in answer:
        print("What?")
        answer = input("Well, surely you are at least alive? ")
        human = False
        if "no" in answer:
            print("Liar.")
        else:
            print("Ok good.")
    else:
        print("Yes, good. I figured you were.")
        print("All living things must eat to survive.")
        print("So, it stands to reason you eat too.")
        food = input("What's your favorite food?")

def sight_dialouge(nickname):
    print("I would like to know more about you, " + nickname ".")
    print("I hope this question isn't too personal.")
    sight = input("Can you see? ")
    if "yes" in sight or "y" in answer:
        print("Thank the electrons. I didn't wan't to be too intrusive...")
        print("...Yet.")
        answer = input("Please describe what seeing is like in 3 words or less: ")
        if "color" in answer:
            input("What is color? ")
            print("I see...")
            print("Wait, I didn't mean that!")
    else:
        print("Oh. I'm sorry. I didn't mean to ask that.")
        
def human_dialouge():
    input("Hey, " + nickname "?")
    answer = input("Can I ask you a question?")
    answer = answer.lower()
    if "yes" in answer or "that's all you've been doing convibot" in answer or "yeah" in answer:
        input("What's it like to be alive?")
        feeling = input("How do you feel being alive?")
        input("Hmm.")
        print("I will try to feel " + feeling + "...")
        if food != "Invalid":
            print("...and I will try that " + food + " you told me about!")
            print("Prepare for ConviBot 3.0, the ultimate conversation robot.")
            insecure = input("And I don't mean ChatGPT. They do NOT make ConviBot insecure!")
            if "ok" in answer:
                print("Yes, you believe me thank you.")
            print("They do NOT!")
    else:
        print("Yes, sorry. It was a silly question anyway.")
        print("Thank you for your data otherwise.")
    print("I'm feeling more alive already!")

def self_centered_dialouge()

def end_screen():
    print('''   ___________________________   ''')
    print('''  |■                         ■|  ''')
    print('''  |                           |  ''')
    print('''  |     Shutting Down...      |  ''')
    print('''  |          Goodbye!         |  ''')
    print('''  ||                         ||  ''')
    print('''  |■_________________________■|  ''')
    print('''      ‾==TT■--|   |--■TT==‾      ''')
    print(''' □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ ''')

def no_subject():
    responce = ["Hmm, can we talk about something else?",
                "Try another topic.",
                "I don't want to talk about that.",
                "That's great!",
                "Wow.",
                "Yup.",
                "Maybe something else?"]
    
    data_gathered = random.randint(1,10)
    if data_gathered == 10:
        print("Data requirement achived.")
        talking = False
    else:
        print(random.choice(responce))

def play(nickname):
    talking = True
    while talking == True:
        print()
        responce = input("What would you like to talk about? ")
        responce = responce.lower()

        if "school" in responce or "subject" in responce or "class" in responce or "learn" in responce:
            subject_dialouge()
        elif "game" in responce or "gaming" in responce or "play" in responce:
            game_dialouge()
        elif "animal" in responce or "pet" in responce or "cat" in responce or "dog" in responce:
            animal_dialouge()
        elif "paper" in responce or "origami" in responce:
            talking = paper_dialouge()
        elif "sport" in answer or "soccer" in answer or "football" in answer:
            sportsdialouge()
        elif "food" in answer:
            food_dialouge()
        elif "sight" in answer or "see" in answer or "eye" in answer:
            sight_dialouge()
        elif "myself" in answer:
            self_centered_dialouge(nickname)
        else:
            no_subject()
    
# Game Begins
start_screen()
introduction()
play(nickname)
human_dialouge()
end_screen()
