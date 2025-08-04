# Trevor Bentley        8-1-2025
# Assignment 6: Candy Realm

# this is a version of candyland tht due to copyrights is reneamed candly realm
# it allows 1-4 players CPU or people to move on a board, and play a game

# ----- Imported Modules -----
import time
import random

#----- Required Header -----
print("Candy Realm: An almost Star Wars Story.")
print("By: Trevor Bentley")
print("[COM S 1270 Section 1]")

# ----- Title crawl -----
print("")
print("")
print("")
time.sleep(2)
print("Welcome Aboard to Candy Realm: George Lucas Edition")
print("")
time.sleep(2)
print("A longer time ago in a galaxy far, far away.")
print("")
time.sleep(2)
print("A NEW DULCHE:")
print("")
time.sleep(2)
print("It is a period of Choco-War.")
print("")
time.sleep(2)
print("In-sugar-ent Space ships striking from a Hidden Wonka base.")
print("")
time.sleep(2)
print("Have just won their fist victory against the ")
print("")
time.sleep(2)
print("Evil Diabetic Empire")
print("")
time.sleep(2)
print("Now its up to you to carry the Rolo Rebels")
print("Meet up at the Randezvous and Secure Sugar for all")
print("")
time.sleep(5)

#----- Main Menu FXN -----
def mainmenu():
    while True:
        print("")
        print("Hello Commander, Welcome Back.")
        print("What's on your agenda today?")
        print("[P]rocede to Rendezvous")
        print("[R]ead these manuals, You really should")
        print("[S]tandby")
        print("_-"*35)

        choice= input("Choose your selection: ").strip().lower()
# ----- Play -----
        if choice == "p":
            nohumans, nocpu, copies = setupgame()
            board = buildaboard()
            deck = buildadeck(copies)
            players, positions = setcallsigns(nohumans, nocpu)
            print("Preparing to jump. Please remain seated...")
            game_loop(players, positions, deck, board)
            break

# ----- Instructions ------
        elif choice =="r":
            print("Oh but reading my Chillon's Manual is too much?")
            print("Fine. Searching now...")
            time.sleep(1)
            print("... loading 15% ...")
            time.sleep(1)
            print("... loading 45% ...")
            time.sleep(1)
            print("... loading 85% ...")
            time.sleep(1)
            print("... Initializing ...")
            print("-"*35)
            
            print("Standing orders (Instructions):")
            print("Draw a colored System tile, then procede to that system")
            print("There's four other Rolo Cells competing for glory")
            print("If you have wothy opponets use them, if not we can Run a simulation")
            print("and I'll Augment the rest")
            print("On your move you may draw, shuffle coordinates, or quit")
            print("Hopefully you'll read my manual next, considering its still packaged")

            print("-"*35)
            
# ----- Quit -----
        elif choice == "s":
            print("I'll see you soon, Commander")
            exit()

# ----- other -----
        else:
            print("This is why we read manuals")
            print("Please select a input p, r, s")

# ----- Set up players-----
def setupgame():
    while True:
        try:
            nohumans = int(input("How many Copilots are we expecing [1 - 4]?: "))
            if 1 <= nohumans <= 4:
                break
            else:
                print("Invalid number. Try 1–4.")
        except ValueError:
            print("That's not a number, Commander.")

    nocpu = 4 - nohumans
    print(f"Deploying {nohumans} human(s) and {nocpu} Augmented cruisers.")

    while True:
        try:
            copies = int(input("How many copies of each Coordinate Card [1 - 5]?: "))
            if 1 <= copies <= 5:
                break
            else:
                print("Invalid range. Choose 1–5 copies.")
        except ValueError:
            print("That's not a number, Commander.")

    return nohumans, nocpu, copies

# ----- Board setup -----
def buildaboard(length=20):

    colors = ['R', 'G', 'B', 'Y', 'M', 'C']
    board = ['RENDEZVOUS']
    for _ in range(length):
# ----- FIX THIS -----
        board.append(random.choice(colors))
# ------------------------------------------------------------
    board.append('YUB NUB')
    return board

# ----- Deck Setup------
def buildadeck(copies_per_color):

    colors = ['R', 'G', 'B', 'Y', 'M', 'C']
    deck = []
    for color in colors:
        deck.extend([color] * copies_per_color)
    random.shuffle(deck)
    return deck

# ----- Players -----
def setcallsigns(nohumans, nocpu):
    players = []
    positions = []
    callsigns = ["Red Leader", "Blue Leader", "Gold Leader", "Green Leader"]

    for i in range(nohumans):
        players.append(f"{callsigns[i]} (COPILOT)")
        positions.append(0)

    for j in range(nocpu):
        players.append(f"AI {callsigns[nohumans + j]} (AI NAVI)")
        positions.append(0)

    return players, positions

# ----- Actual board thing -----
def display_board(board, positions):
    print("\nSECTOR MAP:")
    for tile in board:
        print(f"{tile:^5}", end=" ")
    print()

# ----- Displaing Player Progression -----
    for i in range(len(board)):
        markers = ""
        for p in range(len(positions)):
            if positions[p] == i:
                markers += str(p + 1)
        print(f"{markers:^5}", end=" ")
    print("\n")

# ----- Turn FXN ---

def play_turn(player_index, players, positions, deck, board):
    name = players[player_index]
    current_pos = positions[player_index]
    is_ai = name.startswith("AI ")

    print(f"\n{name}, you are go for action.")

    if is_ai:
        action = random.choice(['d', 's'])
        print(f"{name} chooses to {'draw coordinates' if action == 'd' else 'shuffle coordinates'}...")
        time.sleep(2)
    else:
        while True:
            action = input("[D]raw coordinates, [S]cramble the nav deck, or [Q]uit mission?: ").strip().lower()
            if action in ['d', 's', 'q']:
                break
            print(f"Invalid input, {name}. Try D, S, or Q.")

# ----- quit on turn -----
    if action == 'q':
        print(f"{name} has ejected from the mission. Diserion is death.")
        exit()
# ----- Shuffle -----
    if action == 's':
        random.shuffle(deck)
        print(f"{name} has scrambled the coordinate nav deck!")
        return
#----- missingno -----
    if action == 'd':
        if not deck:
            print("Deck is empty! Reassembling backup coordinates...")
            deck[:] = buildadeck(3)
            random.shuffle(deck)

        drawn = deck.pop(0)
        print(f"{name} draws: {drawn}")

# ----- movement of piece -----
        for i in range(current_pos + 1, len(board)):
            if board[i] == drawn:
                positions[player_index] = i
                print(f"{name} navigates to {drawn} sector at tile {i}!")
                return

        print(f"No match ahead. {name} holds position at tile {current_pos}.")

# ----- Loop to progress the actual game -----
def game_loop(players, positions, deck, board):
    while True:
        for i in range(len(players)):
            display_board(board, positions)
            play_turn(i, players, positions, deck, board)

# ----- Check for win -----
            if board[positions[i]] == "YUB NUB":
                print(f"\n🚀 {players[i]} has reached YUB NUB and secured sweet victory!")
                print("Mission Accomplished. All wings, return to base.")
                return
# ----- Main FXN -----
if __name__ == "__main__":
    mainmenu()
