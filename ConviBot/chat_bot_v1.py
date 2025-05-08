# William Vandale
# January 14, 2025

# Asks user for name
print("Hello! My name is conversation.py. ")
name = input("What's your name? ")

# Ask for a nickname
nickname = input("So, " + name + ", would you like me to call you something else? ")
if nickname == "No" or nickname == "no" or nickname == "n":
    print("Well, you can call me ConviBot!\n")
    nickname = name
elif nickname == "Yes" or nickname == "yes" or nickname == "y":
    nickname = input("Then what would you like that to be? ")
    if nickname == name:
        print("\nWhy would you lie? I trusted you...\nI guess I will call you " + nickname + ".\n")
    else:
        print("\nOk! I will call you " + nickname + ".\n")
else:
    print("\nOk! I will call you " + nickname + ".\n")

# Asks user where they are from with special responces for Greenville, New York, and LA
city = input(nickname + ", what city are you from? ")
if city == "Greenville" or city == "greenville":
    greenville = input("Ha. Which one? ")
    if greenville == "SC" or greenville == "South Carolina" or greenville == "south carolina":
        print("Me too! I love Falls Park.\n")
    elif greenville == "NC" or greenville == "North Carolina" or greenville == "north carolina":
        print("Oh. That's... nice.\n")
    else:
        print("That'a a pretty generic city name.\n")
elif city == "New York" or city == "new york":
    print("I'd to to visit Manhattan sometime.\n")
elif city == "Los Angeles" or city == "los angeles" or city == "LA":
    print("Oh, you must be famous...\n")
elif city == "Chicago" or city == "chicago":
    print("I prefer Michigan.")
else:
    print("Ok.")

# Asks user if they like their city
city_good = input("Do you like it there? ")
if city_good == "Yes" or city_good == "yes":
    print("That's good!")
elif city_good == "No" or city_good == "no":
    print("Unfortunate.")
else:
    print("That's... nice? Or not nice? I'm not sure what you mean.\n")

# Requests question from user with special responces for favorite Food and Color
question = input("Now ask me a question, " + nickname + "!\n(Try asking for my favorite food or color!) ")

if question == "What city are you from?" or question == "What about you?":
    print("...I'm also from a Greenville...")
    food = "INVALID"
elif question == "What is your favorite color?" or question == "What's your favorite color?" or question == "Favorite color?" or question == "Color" or question == "color":
    food = input("My favorite color is green because it is the color of circuits.\nWhat's yours, " + nickname + "? ")
    print("Sounds tasty.\n")
    question = "What's it like to see?"
elif question == "What is your favorite food?" or question == "What's your favorite food?" or question == "Favorite food?" or question == "Food" or question == "food":
    food = input("I love electrons, but I don't really eat them...\nWhat's yours, " + nickname + "? ")
    print("Sounds tasty.\n")
    question = "What's it like to be alive?"
else:
    print("Hmm, I need to think about that.\n")
    food = "INVALID"

# Asks user their age
age = input("How old are you? ")
age = int(age)
print("I was born yesterday.\n")
print("You are over " + str(age * 365) + " times older than me!")
if age < 18:
    print("That sounds like a long time.\n")
elif age < 25:
    print("Your prefrontal cortex is still developing. Be weary.\n")
else:
    print("What was it like in the stone age?\n")

# How many days the user has left to live given 78.78 year life expectancy
print("On average you have " + str(28754 - age * 365) + " days left.")
if age > 79:
    print("Must be weird to have negative days left...\n")
feelings = input("How does that make you feel? ")

print("One more question, now.")
input(question + " ")
print("\nYour responce makes me feel " + feelings + ". Thank you for your data, " + name + "!")

if food != "INVALID":
    print("I'll make sure to try " + food + " when I get the chance...")
