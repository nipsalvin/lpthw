from sys import exit

def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if choice <= 2 :
        how_much = int(choice)
    else:
        dead("Man, learn to type your numbers.")

    if how_much <= 50:
        print("Nice you are not greedy, you win!")
    elif how_much > 50:
        dead
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is infront of another door.")
    print("How are you going to move the bear? ")
    print("""
    A. Take honey
    B. Taunt bear
    \n a or b
    """)
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "a":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "b" and not bear_moved:
            print("The bear has moved from the door.")
            print("you can now go through.")
            bear_moved = True
        elif choice == "b" and bear_moved:
            dead("The bear gets pissed off and eats your legs.") 
        elif choice == "yes" and bear_moved:
            print("do you open the door written Gold Room??")
            gold_room()
        else:
            print(" have no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Medusa")
    print("She, it, whatever hears a sound and turns around.")
    print("Do you get scared and run or try get a glimpse of her face before you get out ??")
    print("""
    A. Run without looking back
    B. Peek first
    \n a or b ?
   """ )

    choice = input("> ")

    if "a" in choice:
        start()
    elif "b" in choice:
        dead("You immediately start turning into concrete ")
    else:
        cthulhu_room()


def dead(why):
    print(why, "\nGame over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and  left.")
    print("which one do you take? ")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room till you starve.")


start()




