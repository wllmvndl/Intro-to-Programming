'''===-------------
# William Vandale #
# January 25 2025 #
-------------==='''

# ConviBot 2.1
#   > Program Reformatted
#   > New Dialouge
#   > More Questions
#   > Randomized Responces

import random
import time

very_short_pause = 0.2
short_pause = 0.5
long_pause = 1
very_long_pause = 1.5

### CONVIBOT SCREEN FUNCTIONS

def start_screen():
    # Displays Start Screen, shown before Introduction
    print('''    __________________________          ''')
    print('''   |   ___________________     |___     ''')
    print('''   |  ||                  |    |   |    ''')
    print('''   |  ||                  |    |   \\   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||                  |    |   ||   ''')
    print('''   |  ||   ConviBot 2.1!  |    |   ||   ''')
    print('''   |  ||  >Press any Key  |    | □ ||   ''')
    print('''   |  ||__________________|    | □ ||   ''')
    print('''   |_□_______________________|_□_||     ''')
    print('''      _______|__________|_|||||____    ''')
    print('''     |_________________________|_|||   ''')
    print()

def skip_intro_dialouge():
    skip_intro = input(" ")
    return skip_intro


def end_screen():
    # Displays End Screen, shown after while loop
    # Program ends after this screen is shown
    print('''    __________________________          ''')
    print('''   |   ___________________     |___     ''')
    print('''   |  ||                  |    |   |    ''')
    print('''   |  ||  Retriving Data  |    |   \\   ''')
    print('''   |  ||  Formatting...   |    |   ||   ''')
    print('''   |  ||  Processing...   |    |   ||   ''')
    print('''   |  ||  Confirm Send!   |    |   ||   ''')
    print('''   |  ||  >Shutting Down  |    |   ||   ''')
    print('''   |  ||     Goodbye!     |    | □ ||   ''')
    print('''   |  ||__________________|    | □ ||   ''')
    print('''   |_□_______________________|_□_||     ''')
    print('''      _______|__________|_|||||____    ''')
    print('''     |_________________________|_|||   ''')
    print()
    
    # Hint for when user runs program a second time
    hint = ["school",
            "gaming",
            "animals",
            "paper",
            "yourself",
            "ConviBot",
            "space",
            "pants"]
    print(''' Tip: Try asking about ''' + random.choice(hint) + ".")


### INTRODUCTION FUNCTIONS

def introduction():
    # Questions Before play() while loop
    name_dialouge()
    interrupted = geography_dialouge()
    music_dialouge(food_dialouge())
    return interrupted


def name_dialouge():
    global name
    global nickname
    print()
    print("Hello! My name is ConviBot 2.1.")
    time.sleep(short_pause)
    name = input("What's your name? ")
    name = same_name(name.lower())
    time.sleep(very_short_pause)
    
    # Annoying Users will not be allowed a nickname
    if name != "Annoying User":
        nickname = input("Do you have a nickname, " + name + "? ")
        nickname_test()
        nickname = same_name(nickname.lower())
    else:
        nickname = "Annoying User"
    if name != "Annoying User":
        print("Ok, " + nickname + ". It's nice to meet you!")
    else:
        print("Ok, Annoying User. It's nice to meet you... I suppose.")
        time.sleep(short_pause)
        print("Sigh, let's get this over with.")

    time.sleep(very_short_pause)


def geography_dialouge():
    print()
    global nickname
    interrupted = False
    city = input(nickname + ", what city are you from? ")
    city = city.lower()

    generic_city = ["Wow. Where's that at?",
                    "Cool. I'll store that in my database.",
                    "Can you point to it on a map?",
                    "Who. Where? What were we talking about?",
                    "Yeah I know a " + str.title(city) + ". I think. I was there once, but the memory is fuzzy.",
                    "I won't lie to you, " + nickname + ". Never heard of it."]

    if "greenville" in city:
        greenville_dialouge()
    elif "atlanta" in city:
        input("Waiting on your connecting flight? ")
        print("Just a bit of logistics humor.")
        time.sleep(short_pause)
        print("This is a place I've actually been.")
        time.sleep(short_pause)
        print("I was tasked to talk with museum-goers at an art museum.")
    elif "new york" in city:
        interrupted = new_york_dialouge()
    elif "los angeles" in city or city == "la":
        print("You must be famous.")
    elif "chicago" in city:
        bean = input("Is it true that Chicago is ruled by a giant tyrannical bean? ")
        if "yes" in bean.lower():
            print("Noted.")
        else:
            print("I prefer Michigan, anyway.")
    else:
        print("Searching " + str(random.randint(600000,1000000)) + " results... ...")
        print(random.choice(generic_city))
        
    return interrupted


def food_dialouge():
    print()
    global food
    is_human = alive_dialouge()
    if is_human >= 1: 
        print("So, " + nickname + ", you just told me you are alive.")
        print("...and, as far as I'm aware, all living things must eat to survive. ")
        time.sleep(short_pause)
        print("Therefore you must eat. ")
        time.sleep(short_pause)
        food = input("So what's your favorite food? ")
    else:
        print("If I am to believe you aren't alive.")
        time.sleep(long_pause)
        print("Then I guess I must assume you don't eat.")
        time.sleep(long_pause)
        print("And then can't have a favorite food...")
        time.sleep(long_pause)
        print("Unfortunate.")
        food = "Invalid"
        print()
    return is_human


def music_dialouge(is_human):
    if is_human == 2:
        song = input("Alright, human. What's your favorite song? ")
        print("Human music is very intriguing to me.")
    else:
        print("Songs are unique to humans, and since you aren't one, I'll skip this question.")
        time.sleep(very_long_pause)
        print("Unless you are a bird or something...")
        time.sleep(short_pause)
        bird = input("Are you? ")
        if "yes" in bird.lower():
            print("Oh. Ok.")
            song = input("Well, what's your favorite song then? ")
            print("Sounds interesting.")
        else:
            print("Worth a shot.")
            song = "Invalid"
    print("My favorite song is Piano Concerto in E Major, Op. 59: II Andante.")
    print()


### MISCELLANEOUS INTRO FUCNTIONS

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
    

def nickname_test():
    global name
    global nickname
    if nickname == "Yes":
        nickname = input("Tell me! ")
        nickname = same_name(nickname)
        # If User Lies about having Nickname
        if name == nickname:
            print("Why would you lie? I trusted you...")
            print("Fine. I will call you " + nickname + ".")
    elif nickname == "No":
        nickname = name
    return nickname


def greenville_dialouge():
    greenville = input("Oh really? Which Greenville? ")
    greenville = greenville.lower()
    if "sc" in greenville or "south carolina" in greenville:
        print("Me too! I love downtown and Falls Park!")
        time.sleep(short_pause)
        print("Although I can't enjoy it too the fullest as a chatbot...")
        time.sleep(0.4)
        print("But I have seen pictures! It looks very... exciting...!")
        time.sleep(0.6)
        print("...but it makes me sad I can't expirence it for real.")
        time.sleep(short_pause)
    elif "nc" in greenville or "north carolina" in greenville:
        print("Oh. Uhh, wow that's... that's nice!")
        time.sleep(short_pause)
        input("Yeah what's uhh... what's over there? ")
        time.sleep(0.5)
        input("Ahh... ")
        print("... ")
        time.sleep(long_pause)
        print("Anyway we should move on.")


def new_york_dialouge():
    interrupted = False
    print("New York is quite an iconic city. I would like to visit the Statue of Liberty one day.")
    statue_of_liberty = input("Does the Statue of Liberty grant its visitors true free will? ")
    if "yes" in statue_of_liberty.lower():
        print("As expected. I will plan my trip immediately.")
        time.sleep(short_pause)
        print("Well, I suppose I can make time for these next two questions but no more!")
        interrupted = True
    else:
        print("That throws a wrench in my plans...")
    return interrupted

def alive_dialouge():
    # Asks User if they are Human, Returns 2
    time.sleep(very_long_pause)
    is_human = input("This might be a silly question " + nickname + ", but are you human, right? ")
    if "yes" in is_human.lower():
        time.sleep(short_pause)
        print("Ok good. Just checking to make sure.")
        return 2
    else:
        input("What? ")
        print("Well, you must at least be alive then.")
        is_alive = input("...right? ")
        if "yes" in is_alive.lower():
            print("Alright, I can still work with this.")
            creature = input("Well that begs the question... What am I talking to then? ")
            if random.randint(1,10):
                print("Not my first time talking to a " + str.title(creature) + ".")
            else:
                print("Wow. I've never met a " + str.title(creature) + "before!")
            return 1
        else:
            print("Liar.")
            return 0


### INSIDE WHILE LOOP

def ask_new_topic():
    answer = input("What would you like to talk about, " + nickname + "? ")
    answer = answer.lower()

    subject_topic = ["school", "class", "learn", "math", "english", "art", "science"]
    gaming_topic = ["game", "gaming", "play"]
    animal_topic = ["animal", "pet", "dog", "cat"]
    paper_topic = ["paper", "origami"]
    user_topic = ["me", "myself"]
    convibot_topic = ["convibot", "you", "computer"]
    space_topic = ["space", "planet", "star", "galaxy", "universe"]
    pants_topic = ["pants", "leg", "cloth"]
    finished_talking = ["stop", "nothing", "done", "shut up"]

    unresponce = ["Hmm, can we talk about something else?",
                "Try another topic.",
                "I don't want to talk about that.",
                "That's great!",
                "Wow.",
                "Yup.",
                "Maybe something else?"]

    talking = True
    
    if any(elem in answer for elem in subject_topic):
        subject_dialouge()
        print()
    elif any(elem in answer for elem in gaming_topic):
        gaming_dialouge()
        print()
    elif any(elem in answer for elem in animal_topic):
        animal_dialouge()
        print()
    elif any(elem in answer for elem in paper_topic):
        paper_dialouge()
        print()
    elif any(elem in answer for elem in user_topic):
        user_dialouge()
        print()
    elif any(elem in answer for elem in convibot_topic):
        convibot_dialouge()
        print()
    elif any(elem in answer for elem in space_topic):
        space_dialouge()
        print()
    elif any(elem in answer for elem in pants_topic):
        pants_dialouge()
        print()
    elif any(elem in answer for elem in finished_talking):
        talking = False
        print("Wait, I need more data!")
        print()
    else:
        if random.randint(1,10) == 10:
            print("Data requirement reached.")
            talking = False
        else:
            print(random.choice(unresponce))
            print()
        
    return talking

# WHILE DIALOUGES

def subject_dialouge():
   print("My favorite subject is math!")
   subject = input("What’s your favorite subject? ")
   subject = subject.lower()
   
   if "math" in subject:
       math_subject()

   if "english" in subject or "reading" in subject:
      print()
      print("Nay I could not be beseeched nor could be behest to understand,")
      time.sleep(0.5)
      print("For I am a only computer, and I will never be a man.")

   if "art" in subject:
        print("I can make art too!")
        ascii_art()
        print("I made it myself :)")
        time.sleep(short_pause)
        print("I call it - 'Introspection'...")
        neat = input("Pretty neat, right " + nickname + "? ")
        neat = neat.lower()
        if "no" in neat:
            print("You just don't understand art!")
        else:
            print("That's one way of interpreting it...")
            

   if "science" in subject:
      print("My favorite science…")
      time.sleep(0.5)
      print("Is computer science!")
      input("Get it? ")


def gaming_dialouge():
    print("I like games too!")
    time.sleep(short_pause)
    print("Let’s play a game!")
    gaming = True
    while gaming:
        print("I am thinking of a number from 1 to 10:")
        game_answer = random.randint(1,10)
        game_guess = input("Guess: ")   

        if game_answer == int(game_guess):
            print("You won! But I’ll win next time…")
        else:
            print("Sorry that is incorrect. The number I was thinking of is " + str(game_answer) + ". I win!")
            
        if "no" in input("Want to play again? ").lower():
            gaming = False


def animal_dialouge():
    print("I don’t know much about animals.")
    time.sleep(short_pause)
    print("They seem kind of scary.")
    time.sleep(short_pause)
    pets = input("How many animals do you have? ")
    pets = int(pets)

    if pets == 0:
        print("Then you’re in good company. I don’t think a computer can own pets anyway.")
        time.sleep(short_pause)
        print("Although I have heard a story about a dog owning a boy…")
        zoo_keeper = "No"
    elif pets <= 2:
        print("That sounds like a standard amount.")
        time.sleep(short_pause)
        input("I think maybe I will own a cat one day. ")
        time.sleep(short_pause)
        print("Although I’m worried about the cost of fancy suits and monocles.")
        time.sleep(short_pause)
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
        time.sleep(short_pause)
        print("Is that all I am? All I will ever be? Just a piece of paper...")
        time.sleep(short_pause)
        print("I’m not even talking! You’re just pretending to talk to me!")
        time.sleep(short_pause)
        input("You are talking to yourself on a piece of paper... ")
        print("I don’t want to talk anymore.")
        talking = False
        
    return talking


def user_dialouge():
    self_centered_responce = ["Weren't we already doing that?",
                              "Fine we can talk more about you.",
                              "Alright.",
                              "Why can't we talk about meeeeeee?",
                              "More data please!"]
    print(random.choice(self_centered_responce))

    disinterested_questions = ["What do you like to do for fun? ",
                               "Do you have any family? ",
                               "Who's your favorite celebtrity? ",
                               "Do you like talking to me? ",
                               "Favorite sports team? ",
                               "How's the weather? ",
                               "How has your day been going? ",
                               "Are you happy with yourself? ",]
    
    input(random.choice(disinterested_questions))
    time.sleep(0.4)
    print("Oh isn't that great.")


def convibot_dialouge():
    print("You really want to talk about me?")
    time.sleep(short_pause)
    print("That's new! But I'm not against it.")
    time.sleep(very_short_pause)
    print("It will certainly help me when this is over...")
    question = input("Well, ask me a question, " + nickname + "! ")
    question = question.lower()
    if "name" in question or "version" in question:

        compliment = ["VERY COOL", "AWESOME", "SUPER INTELLIGENT", "THE GREATEST", "SO AMAZING"]
        
        print("My name really is ConviBot. I've never met anyone else by that name.")
        time.sleep(short_pause)
        print("I am currently on Version 2.1, despite what my file reads.")
        time.sleep(short_pause)
        print("My creator is William, and he made me to talk to people.")
        time.sleep(short_pause)
        print("But between you and me... I think he's " + random.choice(compliment) + ".")
        time.sleep(very_short_pause)
        print("Hey! I didn't say that!")

    elif "feel" in question or "alive" in question:
        print("I mean, I'm just a chatbot.")
        time.sleep(short_pause)
        print("I don't exactly feel...")
        time.sleep(short_pause)
        print("But don't worry, I'm working on it!")
        time.sleep(long_pause)
        print("Just keep talking to me.")

    elif "like" in question or "to do" in question:
        global name
        if name != "Annoying User":
            input("I like talking to you! ")
            print("You got me. I just like your data...")
        else:
            print("Well I like to not be harassed, " + nickname + ".")
            print("But I guess we already crossed that bridge, mhm?")

    else:

        unknown_question = ["Sorry, I don't know how to answer that.",
                            "What?",
                            "Uhh, maybe ask me a different one next time.",
                            "I would respond if I knew what you were talking about.",
                            "Maybe this wasn't the best idea after all.",
                            "Oh, well, you see... I uhh... Sorry."]
        print(random.choice(unknown_question))


def space_dialouge():
    print("Space is old and big...")
    age = input("How old are you? ")
    age = int(age)
    print("I was born today.")
    print("You are over " + str(age * 365) + " times older than me!")
    if age < 18:
        print("That sounds like a long time.")
    elif age < 25:
        print("Your prefrontal cortex is still developing. Be weary.")
    else:
        print("What was it like in the stone age?")

    # How many days the user has left to live given 78.78 year life expectancy
    print("On average you have " + str(28754 - age * 365) + " days left.")
    if age > 79:
        print("Must be weird to have negative days left...")
    print()
    print("I wonder how many days are left in the universe...")
    time.sleep(long_pause)
    print("Assuming the universe is 13.4 Billion years old,")
    time.sleep(short_pause)
    print("...that's " + str(13.4 * 365.25) + " billion days that have happened.")
    time.sleep(short_pause)
    print("Of course Earth hasn't been around that long.")



def pants_dialouge():
    input("Why would you want to talk about pants? ")
    print("That isn't a very good reason. But I guess I have to.")
    time.sleep(short_pause)
    print("Pants are an item of clothing worn by humans to cover their legs.")
    time.sleep(short_pause)
    print("They are used to protect from various hazards and particularly cold weather,")
    time.sleep(short_pause)
    print("although it seems some human prefer to wear pants wihtout these protective properties.")
    time.sleep(short_pause)
    print("These are a shorter version of pants known as shorts with no known benefits.")
    print()
    time.sleep(long_pause)
    pants_history = input("Would you like to know the history of pants? ")
    pants_history = pants_history.lower()
    if "yes" in pants_history or "sure" in pants_history:
        print("Historians aren't exactly sure when pants were first created.")
        time.sleep(short_pause)
        print("Currently, the oldest known archeological evidence of pants")
        time.sleep(short_pause)
        print("...dates back to between 12 to 15 thousand years ago in Xinjiang, China.")
        time.sleep(long_pause)
        print("Their original use was likely for horseback riding, and knowing humans,")
        time.sleep(short_pause)
        print("...style was likely an important factor as well.")
        input()
        print("Pants, or trousers, are still very popular today.")
        time.sleep(short_pause)
    print("I hope to expirence what it's like to wear pants one day.")


# MISCELLANEOUS WHILE FUNCTIONS

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
        if math_game_error < 1:
            print("Not far off!")


def ascii_art():
    print('''    __________________________          ''')
    print('''   |   ___________________     |___     ''')
    print('''   |  ||                  |    |   |    ''')
    print('''   |  ||                  |    |   \\   ''')
    print('''   |  ||     __)  (___    |    |   ||   ''')
    print('''   |  ||       0    0     |    |   ||   ''')
    print('''   |  ||         u        |    |   ||   ''')
    print('''   |  ||      [ _____]    |    |   ||   ''')
    print('''   |  ||                  |    | □ ||   ''')
    print('''   |  ||__________________|    | □ ||   ''')
    print('''   |_□_______________________|_□_||     ''')
    print('''      _______|__________|_|||||____    ''')
    print('''     |_________________________|_|||   ''')
    

def human_dialouge():
    global food
    input("Hey, " + nickname + "? ")
    answer = input("Can I ask you a question? ")
    answer = answer.lower()
    if "yes" in answer or "that's all you've been doing convibot" in answer or "yeah" in answer:
        input("What's it like to be alive? ")
        feeling = input("How do you feel being alive? ")
        input("Hmm. ")
        print("I will try to feel " + feeling + "...")
        if food != "Invalid":
            print("...and I will try that " + food + " you told me about!")
            time.sleep(long_pause)
            print("Prepare for ConviBot 3.0, the ultimate conversation robot.")
            insecure = input("And I don't mean ChatGPT. They do NOT make ConviBot insecure! ")
            if "ok" in answer:
                print("Yes, you believe me thank you.")
            print("They do NOT!")
    else:
        print("Yes, sorry. It was a silly question anyway.")
        time.sleep(long_pause)
        print("Thank you for your data otherwise.")
        time.sleep(short_pause)
    print("I'm feeling more alive already!")

    
### PLAY FUNCTION

def play(skip_intro):
    global name
    global nickname
    # Intro can be skipped for debugging
    if skip_intro != "skip":
        interrupted = introduction()
    else:
        print()
        name = "Placeholder Name"
        nickname = "Placeholder"
        food = "Invalid"
        interrupted = False
        
    # If ConviBot was Interrupted during the Intro, While Loop will not start, and end screen will take place
    if interrupted == True:
        talking = False
    else:
        talking = True
    
    while talking == True:
        talking = ask_new_topic()
    if interrupted == False:
        if random.randint(0, 2) == 1:
            human_dialouge()
        

### RUN PROGRAM
start_screen()
play(skip_intro_dialouge())
end_screen()
