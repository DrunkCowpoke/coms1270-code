# Trevor Bentley                7-2-2025
# 
#lab 4: this code tells a choose your ending story

import time

def main():
    print("You find yourself gaining conscious in an alley on Mos Eisley")
    print("You start seeking out a glass of blue milk, preferably in a droid free establishment")
    print("Some random Jawa starts screaming ''Utinni''")
    print("You have to do something, do you [wave], [ignore] and walk away, or Just Start Blastin [JSB]?")
    
    fork1= input("Whats it going to be?")

# ----- Split 1 -----

    if fork1.lower() == "wave":
        print("looks like youre getting jumped by Jawas today, they approach weapons drawn")
        print("Do you [run], scream [utinni], or offer [trade]?")
        fork2= input("Whats your call?")

        if fork2.lower() == "run":
            print("You make it down the block to a dead end, rather iroic. ")
            print("They steal your credits and your left shoe.")

        elif fork2.lower() == "utinni":
            print("The Jawas freeze. After a breif huddle they face you again.")
            print("You are now the proud leader of a black market Jawa Gang.")

        elif fork2.lower() == "trade":
            print("Are the Jawas laughing at you? you try handing them a power cell")
            print("You get zapped. coming to you find yourself in a Bantha trough.")
            print("did the Jawas just steal your kidneys?[y/n]")
            fork3= input("yes or no")

            if fork3.lower()== "yes":
                print("No, you silly goose they only took a lung")
            else:
                print("Tough break, you should get that looked at")
        else:
            print("You are hit with stray blaster fire from a nearby squabble.")

# ----- Split 2 -----

    elif fork1.lower() == "ignore":
        print("What are you a nerf herder? you dont turn your back on Jawas.")
        print("Are you [run]ning at least? do you see a security [droid]? Even an open [door] is an option")
        fork2= input("Choose carefully")

        if fork2.lower() == "run":
            print("You run directly into an Imperial Captain")
            print("He looks like hes not happy even with that goofy helmet.")
            print("Best of luck from the detention block")

        elif fork2.lower() == "droid":
            print("Dude this is the outter rim, thats a bounty droid")
            print("Should be fine, a little banged up maybe,")
            print("I mean you are clean right?[Y/N]")
            fork3=input("Do you have an open criminal record?")

            if fork3.lower() == "yes":
                print("Not exactly a surprise on Tatooine.")
                print("You get dragged off for a few credits")
            else:
                print("The droid takes you anyway, you must have a criminal twin")
            
        if fork2.lower() == "door":
            print("Congrats you found a Cantina")
            print("You get your blue milk and take the window seat")
            print("You can see the Jawas waiting for you.")
            time.sleep(5)
            print("Its not over, but at least you got the milk.")


# ----- Split 3 -----

    elif fork1.lower() == "jsb":
        print("What are you doing? they are just used car salsemen dude?")
        print("The noise attracts the nearby garrison")
        print("You stay put thinking they'll save you")
        print("Unfortunately the Jawas had already paid off the garrison")
        print("lets just say there isnt a detention block at the moment")

#----- the else -----

    else:
        print("You stand there dumbfounded. The Jawas view that as intimidation")
        print("you think it's surprizingly effective. They scatter")
        print("just as you think your luck is turning,")
        print("You get run over by some farm kid and a hobo in a speeder.")
        print("the jawas then take your wallet and socks")


if __name__ == "__main__":
    main()
