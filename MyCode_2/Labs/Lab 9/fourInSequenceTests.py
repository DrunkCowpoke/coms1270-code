# Trevor Bentley    7-24-2025
# Lab 9: fourInSequenceTests.py

# This code is meant to test my four in seqence file functions. lord have mercy on my code

# ----- Importing the FXNs -----
from fourInSequence import (checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner, createBoard, dropPieceIntoBoard,)


# ----- Next Move Test -----
def test_checkForNextMoveWin():
    board = createBoard(4, 4)
    dropPieceIntoBoard(board, 0, 1)
    dropPieceIntoBoard(board, 1, 1)
    dropPieceIntoBoard(board, 2, 1)
    
    assert checkForNextMoveWin(board, 1) == 3

# ----- Check Adjacent Test -----
def test_checkAdjacent():
    board = createBoard(4, 4)
    dropPieceIntoBoard(board, 1, 1)
    result = checkAdjacent(board, 1)

    assert result in [0, 1, 2]

# ----- Check Draw Test -----

def test_checkDraw():
    board = createBoard(4, 4)
    for col in range(4):
        for _ in range(4):
            dropPieceIntoBoard(board, col, 1)
    
    assert checkDraw(board) == True

# ----- Winner Test -----
def test_checkWinner():
    board = createBoard(4, 4)
    dropPieceIntoBoard(board, 0, 1)
    dropPieceIntoBoard(board, 1, 1)
    dropPieceIntoBoard(board, 2, 1)
    dropPieceIntoBoard(board, 3, 1)

    assert checkWinner(board, 1) == True

