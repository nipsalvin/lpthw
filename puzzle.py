#This is for the puzzle game
from sys import exit


def gold_room():
    print("You enter in a room full of gold. How much do you take?")

    choice = input("How many Kilos (1 - 100) \n> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You meet the spider as you leave but you can't escape because of the weight of the gold.\nIt catches you an eats you.")



def bear_room():
    print("There is bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?\n")
    print("""Type A if you choose to steal the honey.
Type B if you choose to taunt the bear.""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "a":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "b" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.\n")
            print("The bear moves slowly then stops and sits to continue eating the honey.")
            print("Do you 'A' taunt it again or 'B' open the door and get in")
            print("Pick A or B.\nBest of luck")
            bear_moved = True


        elif choice == "a" and bear_moved:
            dead("You taunt the already leaving bear again."
            "The bear gets pissed off and chews your leg off.")
        elif choice == "b" and bear_moved:
            gold_room()
        else:
            print("Please pick 'A' or 'B'.")


def medusa_room():
    print("Here you see the great evil Medusa.")
    print("She...it, whatever, hears a sound and begins to turn around.")
    print("Do you flee for your life or try see what kind of evil she is?")
    
    print("Type A if you choose to flee. Type B if you choose to look ")
    choice = input("> ")

    if "a" in choice:
        start()
    elif "b" in choice:
        dead("Your legs start to turn into concrete as soon as you see her face.\nYou watch yourself slowly turn into stone as she slithers closer to devour you.")
    else:
        medusa_room()


def dead(why):
    print(why, "GAME OVER !!")
    exit(0)

def start():
    print("You are in a dark room as the a giant spider creeps towards you \n with murderous intent")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("Choose A for left and B for right")

    choice = input("> ")

    if choice == "a":
        bear_room()
    elif choice == "b":
        medusa_room()
    else:
        dead("Too slow, the spider got you")

start()


