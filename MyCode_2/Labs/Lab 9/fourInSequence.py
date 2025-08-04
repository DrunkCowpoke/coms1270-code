# Trevor Bentley             7-18-2025
# Assignment 4
# Four in Sequence is Connect 4, but its python and avoiding copyrights 

# CITATION: Much of the code in this assignment is heavily modified/ adapted from code originally created by ChatGPT
# CITATION: ACCESSED: 3-15-2023
# CITATION: URL: https://chat.openai.com

import random
import sys

# ----- This is basically a header -----
def printTitleMaterial():
    
    print("Four In Sequence!")
    print()
    print("By: Trevor Bentley")
    print("[COM S 1270 1]")
    print()
# ----- Main Menu -----
def initialChoice():

    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

# ----- human v machine ------
def chooseNumPlayers():

    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers != 1 and numPlayers != 2:
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers

# ----- Break between games -----
def printBanner():
    """Prints out a nice header to delineate the game from the previous text output.
    """
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

# ----- Piece assignments -----
def getPlayerPiece(playerNumber):

    piece = ""
    if playerNumber == 0:
        piece = "."
    elif playerNumber == 1:
        piece = "X"
    elif playerNumber == 2:
        piece = "O"
    return piece

# -----Board Development -----
def createBoard(width, height):

    empty = getPlayerPiece(0)
    board = []
    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(empty)
    return board
# ----- Board Building -----
# ----- Had to moidify this to actually track whats going on here -----

def printBoard(board):
    print("   " + "   ".join(str(i) for i in range(len(board[0]))))
    print("  +" + "---+" * len(board[0]))
    for row in board:
        print(" | " + " | ".join(row) + " |")
        print(" +" + "---+" * len(board[0]))

    print()
    print()

# ----- Piece Placement -----
def getColumnInt(board, playerNumber):

    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))

# ----- Get in the Zone -----
def getInputInRange(board, playerNumber):

    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col

# ----- Getting choice into the board -----
def getHumanInput(board, playerNumber):

    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col

# ----- Win next move -----
def checkForNextMoveWin(board, playerNumber):
    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)

    # iterate through all columns, assigning each column number to the loop variable
    for col in range(len(board [0])):
        # use getOpenRow() to check if the column has an open row, and return the row number if there is one
        row = getOpenRow(board,col)
        # if the column has an open row, meaning getOpenRow() did not return -1, then perform several logical steps
        if row != -1:
            # set the board, at the location [row][col] to be the player piece found above with the placePiece() function
            placePiece(board,row,col,piece)
            # use checkWinner() to see if there is a winning move that resulted from changing the board on the line above
            if checkWinner (board,playerNumber):
                # if there was a winning move found, reset the board, at the location [row][col] to be the empty piece found above with the placePiece() function
                placePiece(board,row,col,empty)
                # if there was a winning move found, immediately return the current column number
                return col
            # reset the board, at the location [row][col] to be the empty piece found above with the placePiece() function
            placePiece(board,row,col,empty)

    # return -1, as there was no winning move found
    return -1

# ----- Looking both ways -----
def checkAdjacent(board, playerNumber):

    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []
    
    for column in range(0, len(board[0])):
        row = getOpenRow(board, column)
        if row != -1:
            # upper left piece (up one row, left one column)
            #
            # do a check to ensure we don't get an 'index out of range' error
            if row - 1 >= 0 and column - 1 >= 0:
                # do a check to see if the board location under consideration is equal to the piece found above
                if board[row-1][column-1] == piece:
                    # append the column under consideration to the 'adjacents' list
                    adjacents.append(column)

            # left piece (left one column)
            if col - 1 >=0:
            # ensure we don't get an 'index out of range' error
                if board [row][column-1] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list
                    # the comments are below the actual code here

            # lower left piece (down one row, left one column)
            if row + 1 < len(board) and column - 1 >= 0: 
            # ensure we don't get an 'index out of range' error
                if board[row+1][column-1] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list


            # lower piece (down one row)
            if row + 1 < len(board):
            # ensure we don't get an 'index out of range' error
                if board[row+1][column] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list


            # lower right piece (down one row, right one column)
            if row + 1 < len(board) and column + 1 < len(board[0]):
            # ensure we don't get an 'index out of range' error
                if board[row+1][column+1] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list


            # right piece (right one column)
            if column + 1 < len(board[0]):
            # ensure we don't get an 'index out of range' error
                if board[row][column+1] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list


            # upper right piece (up one row, right one column)
            if row - 1 >= 0 and column + 1 < len(board[0]):
            # ensure we don't get an 'index out of range' error
                if board[row-1][column+1] == piece:
                # do a check to see if the board location under consideration is equal to the piece found above
                    adjacents.append(column)
                    # append the column under consideration to the 'adjacents' list

#----- So I feel like we are missing a direction so heres straight up-----
            if row - 1 >= 0 and board[row-1][column] == piece:
                adjacents.append(column)

    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]
        # print("piece:", piece, "adjacents:", adjacents, "randVal:", randVal, "col:", col) # for debugging
    
    return col

# ----- AI playing development -----
def getComputerInput(board, currentPlayerTurn):

    opponentPlayerTurn = switchTurns(currentPlayerTurn)
    
    # NOTE: the various print() statements here which have been commented out will help with debugging.

    # check if there is a winning move - if there is then take it
    col = checkForNextMoveWin(board, currentPlayerTurn)
    # print("WIN")

    # check if the opponent has a winning move - if there is then block it
    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)
        # print("BLOCK")

    # check if there are any adjacent pieces available - try to connect to them
    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)
        # print("ADJACENT")
    
    # if no winning move is available, and no block is available, and no adjacent pieces are available - choose a random column
    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))
        # print("RANDOM")

    # print out a string stating the column that was chosen
    print("Player {0}, please select a column between (0-{1}): {2}".format(currentPlayerTurn, len(board[0]) - 1, col))

    return col

# ----- Checking for gaps -----
def getOpenRow(board, col):

    empty = getPlayerPiece(0)
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == empty:
            return row
    return -1

# ----- Actual placement -----
def placePiece(board, row, col, piece):

    board[row][col] = piece

# ----- Droping piece into board -----
def dropPieceIntoBoard(board, col, playerNumber):

    row = getOpenRow(board, col)
    placePiece(board, row, col, getPlayerPiece(playerNumber))

# ----- Stale Mate -----
def checkDraw(board):

    empty = getPlayerPiece(0)

    # iterate through all the rows in the board
    for row in board:
        # iterate through all the columns in a row
        for col in row:
            # check if the column is empty
            if col == empty:
                # if a column is empty for a particular row, then no draw is possible - return False immediately
                return False
    # if there was not a single empty column found on the entire board, the board must be entirely filled - return True for a draw
    return True

# ----- Victory Laps -----
def checkWinner(board, playerNumber):

# ----- Check for Win ----- 
    # get the piece to check for
    piece = getPlayerPiece(playerNumber)

    # check horizontal locations
    for row in range(0, len(board)):
        for column in range(0, len(board[0]) - 3):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True

    # check vertical locations
    for row in range(0, len(board)- 3):
        for col in range(0, len(board[0])):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True

    # check negatively sloped diagonals
    for row in range(0, len(board) - 3):
        for col in range(0, len(board[0])- 3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True

    # check positively sloped diagonals
    for row in range(3, len(board)):
        for col in range(0, len(board[0])- 3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
# ----- keeping the no winning move return -----
    return False

# ---- end game cycle -----
def resetGameOptions():

    currentPlayerTurn = 1
    winner = False
    draw = False
    return currentPlayerTurn, winner, draw

# ----- Player switch _____
def switchTurns(currentPlayerTurn):

    return ((currentPlayerTurn % 2) + 1)

# ----- Main FXN ----
def main():
    
    # main script running control variable
    running = True
    
    # gameplay variables
    currentPlayerTurn = 1 # can be 1 or 2
    winner = False
    draw = False

    # print the title/ author information
    printTitleMaterial()

    # play the game
    while running:
        choice = initialChoice()
        if choice == "p":

            # reset relevant gameplay variables
            currentPlayerTurn, winner, draw = resetGameOptions()

            # choose number of players
            numPlayers = chooseNumPlayers()

            # create gameboard
            board = createBoard(7, 6)

            # round setup
            printBanner()

            # print board
            printBoard(board)

            # main game loop
            while True:
                
                # get input for dropping a piece inside the board (switch between player 1 and player 2)
                if numPlayers == 1:
                    if currentPlayerTurn == 1:
                        col = getHumanInput(board, currentPlayerTurn)
                    elif currentPlayerTurn == 2:
                        col = getComputerInput(board, currentPlayerTurn)
                    else:
                        print("ERROR: currentPlayerTurn is neither 1 or 2! It is actually: {0}".format(currentPlayerTurn))
                        sys.exit()
                elif numPlayers == 2:
                    col = getHumanInput(board, currentPlayerTurn)
                else:
                    print("ERROR: numPlayers is neither 1 or 2! It is actually: {0}".format(numPlayers))
                    sys.exit()
                
                # update the board with the new piece inside of it
                dropPieceIntoBoard(board, col, currentPlayerTurn)

                # print board
                printBoard(board)

                # check for winner
                winner = checkWinner(board, currentPlayerTurn)

                # check for a draw (all columns filled up completely)
                draw = checkDraw(board)
                
                # check of the game is over - if it is, break out of the gameplay loop
                if winner == True:
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    break
                elif draw == True:
                    print("~~ Draw! ~~")
                    print()
                    break
                else: # if the game is not over, print that the turn is over
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    # switch turns
                    currentPlayerTurn = switchTurns(currentPlayerTurn)
# ----- Instructions -----                   
        elif choice == "i":
            print("~~~~~ How this thing works ~~~~~")
            print(" 1) Pick 1-player to face off against the computer, or 2-player to go head-to-head.")
            print(" 2) You and the other player take turns dropping pieces into the board.")
            print(" 3) First one to line up four pieces in a row so be it: across, up/down, or diagonally, wins.")
            print(" That’s it. Four in a row = game over. Simple.")
            print()
# ----- Quitting -----            p
        elif choice == "q":
            running = False
            print("Quitting already? Fine, be that way.")
# ----- Invalid Inputs -----
        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__":
    main()
