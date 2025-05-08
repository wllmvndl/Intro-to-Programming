# This is my ChatBot.
#
# Jon Cooper
# January 21, 2025

def place_conversation():
    place = input("Where are you from? ")

    if place == "Chicago":
        print("That's awesome. Go Cubs!")
    elif place == "Greenville":
        print("Greenville is such a beautiful city.")
    else:
        print("I'd like to visit " + place + " someday.")

def sports_conversation():
    print("I like sports too.")
    team = input("Who is your favorite team?")

    if team == "Clemson" or team == "Tigers":
        print("Great choice!")
    else:
        print("Boo!")

def food_conversation():
    like_cooking = input("Do you like to cook?")
    
    if like_cooking == "yes":
        food = input("What is your favorite thing to make?")

# Greet the user
name = input("What is your name? ")
print("Hello, " + name + "!")

place_conversation()

answer = input("Tell me something about yourself.")
answer = answer.lower()

if "sports" in answer or "football" in answer:
    sports_conversation()
elif "food" in answer:
    food_conversation()
else:
    print("That's very interesting")

print("Ok. Goodbye")


