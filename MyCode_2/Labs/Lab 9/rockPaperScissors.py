# Trevor Bentley    7-25-2025
# Lab 9: rockpaperscissors.py
# This code sets up for a rock paper scissors game

import random

# ----- CPU -----
def CPUmove():
    return random.choice(["Asteroid", "Falcon", "ISD"])

#----- Winning -----
def Victory(player, computer):
    if player == computer:
        return "Draw"
    
    if (player == "Asteroid" and computer == "ISD") or \
       (player == "Falcon" and computer == "Asteroid") or \
       (player == "ISD" and computer == "Falcon"):
        return player
    else:
        return computer
    
# ----- Gameplay -----
def playRound(playerMove):
    computerMove = CPUmove()
    winner = Victory(playerMove, computerMove)

    if winner == playerMove:
        return "Victory is yours"
    elif winner == computerMove:
        return "There's more machine than man here"
    else:
        return "Do or do not, there is no tie"

# ----- The biggest Main fxn yet.  
def main():
    print("~ Star Wars Shakedown ~")
    print("Choose your move: Asteroid(rock), Falcon(Paper), or ISD(Scissors)")

    rounds = int(input("How many rounds? (odd number): "))
    while rounds % 2 == 0:
        print("Must be an odd number to avoid draws.")
        rounds = int(input("How many rounds? (odd number): "))
# ----- Counter loop-----
    wins = 0
    losses = 0
    ties = 0

    for _ in range(rounds):
        player = input("Your move: ")
        while player not in ["Asteroid", "Falcon", "ISD"]:
            print("Invalid move. Choose Asteroid, Falcon, or ISD.")
            player = input("Your move: ")

        outcome = playRound(player)
        print(outcome)

        if outcome == "Victory is yours":
            wins += 1
        elif outcome == "There's more machine than man here":
            losses += 1
        else:
            ties += 1

        if wins > rounds // 2:
            print("You’ve secured a command post!")
            break
        elif losses > rounds // 2:
            print("The Enemy has captured a command post, take it back")
            break

    print(f"Final Score — Wins: {wins}, Losses: {losses}, Draws: {ties}")

if __name__ == "__main__":
    main()