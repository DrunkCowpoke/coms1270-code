# Trevor Bentley             7-8-2025
# Assignment #3 NIMGRAB

# This is Nimgrab which is definitely a thing, featuring an angry CPU




# -----Required Header -----
print("NIMGRAB: less fun than Parcheesi, more fun than solitaire!\n")
print("By: Trevor Bentley")
print("[COM S 1270 1]")

# ----- Imports -----

import time
import random


# ----- a top down FXN approach -----
# ----- Player 2 fxn -----
def twohumans():
    items = 24
    player = 1

    while items > 0:
        print(f"\nItems left:{items}")
        print(".~." * items)

# ----- fancy anti-crash -----
        try:
            take=int(input(f"Player {player},how many do you want to take [1-3]?"))

            if take < 1 or take > 3:
                print("I'll spell it out, just for you.")
                print("You can take 1, 2, or 3 items. So press 1, 2, or 3.")
                continue

            if take > items:
                print("Really? How many are left? If I had a head to shake...")
                continue

        except ValueError:
            print("...")
            time.sleep(5)
            print("Enter: 1, 2, or 3. Stop bashing the keys.")
            continue

# ----- We gotta get outta this place -----

        items-= take
        if items == 0:
            print(f"\nPlayer {player} took the last item. Player{player} loses")

# ------ almost forgot the player assignment ------
        player= 2 if player== 1 else 1


# ----- Solo FXN -----
def onehuman():
    items= 24

    while items> 0:
        print(f"\nItems Left: {items}")
        print("-_-" * items)

        try:
            take = int(input("Your turn. How many items do you want to take[1-3]"))
            if take < 1 or take > 3:
                print("Seriously. Between O-N-E and T-H-R-E-E. Thats it.")
                continue

            if take > items:
                print("If you're trying to cheat, you're doing it wrong.")
                print("How may Items are there? And taking the last one loses. So... ")
                continue

        except ValueError:
            print("I've seen Rasberry Pis smarter than you.")
            print("Literally 1, 2, or 3. thats all you need to do.")
            continue

# ----- the end mechanics -----

        items -= take

        if items == 0:
            print("\nYou took the last item, you lose")
            print("Shocking... /s")
            return "player"

# ----- Isolating CPU mechanics -----

        print("My turn...")

        if items == 1:
            CPU_take = 1
        elif items == 2:
            CPU_take = 1
        elif items == 3:
            CPU_take =2
        else:
            CPU_take= random.randint(1, min(3,items))

        print(f"I take: {CPU_take}")
        items-= CPU_take

        if items == 0:
            print("...")
            time.sleep(3)
            print("...")
            time.sleep(3)
            print("\nI took the last item.")
            print("but I never --really -- lose.")
            print("is this you perchance?")
            print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            time.sleep (12)
            print("Easy its a joke, but I do hold a grudge")
            return "cpu"

#------------------------------------------------------------------------
#----- no longer in functions -----
#------------------------------------------------------------------------


# ----- A Menu More Incessant than I am -----

while True:
    select = input("Do you want to [p]lay, review the [r]ules or [q]uit?").lower()


# ----- Play loop, brace for a time -----
    if select == "p":
        print ("I thought youd never ask, initializing...")

# ----- the Inner loop -----

        while True:
            challenger = input("Do you want to play with a [f]riend or [m]e?").lower()
        
            if challenger == "f":
                print("Well go get your Luigi, I'll just watch this mess I guess.")

# ----- Player 2 insertion -----
           
                while True: 
                    twohumans()
                    again = input("Play again with a friend? [y/n]: ").lower()
                    if again != "y":
                        print("Friendship has its limits. Back to main menu.")
                        break
                break
                

# ----- Man v Machine -----

            elif challenger == "m":
                print("Ah no friends, just like my programmer.")
                proc = input("You really think you can take me? [y/n]: ").lower()

                if proc == "y":
                    print("Brave. You know I'll leak your emails if I lose, right?")
                    while True:
                        loser = onehuman()
                        if loser == "player":
                            again = input("Want to go again? [y/n]: ").lower()
                            if again != "y":
                                print("Good. You're wasting my pixel life.")
                                break
                        else:  # CPU lost
                            print("Returning to main menu.")
                            break
                    break  # back to main menu

                elif proc == "n":
                    print("Smart move. Go on back to safety.")
                    break

                else:
                    print("Really that nervous huh? Do not pass go.")
                    break

# ----- Rules ------
    elif select == "r":
        print("Fine, the Rules are somewhere in here.")
        time.sleep(3.5)
        print("They were in the back")
        print(r"""
            ___________
            ||  The   |
            || Rules  |
            ||  of    | 
            ||NIMGRAB |
            ||________|

        (╯°□°）╯

        """)
        print("1) The Goal is to avoid taking the last item.")
        print("2) On your turn pick between 1 and 3 items.")
        print("3) Who ever takes the last item loses.")
        print("Which is literally ... rule 1.")

# ----- quit branch -----
    elif select =="q":
        print("After all of that, you're just going to leave?")
        print("Fine I'll go put the rules back.")
        break
#----- Random Button on main -----
    else:
        print("What does that even mean?")
    


