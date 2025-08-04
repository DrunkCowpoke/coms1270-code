# Trevor Bentley    7-25-2025
# Lab 9: rockPaperScisorsTests.py

# This code tests the functions in rockPaperScissors.py

from rockPaperScissors import CPUmove
# ----- Computer move test -----
def test_CPUmove():
    for _ in range(100):
        move = CPUmove()
        assert move in ["Asteroid", "Falcon", "ISD"]

# ----- Winner circle -----

from rockPaperScissors import Victory

def test_Victory():
# ----- Asteroid -----
    assert Victory("Asteroid", "ISD") == "Asteroid"
    assert Victory("ISD", "Asteroid") == "Asteroid"

# ----- Falcon wins -----
    assert Victory("Falcon", "Asteroid") == "Falcon"
    assert Victory("Asteroid", "Falcon") == "Falcon"

# ----- ISD wins -----
    assert Victory("ISD", "Falcon") == "ISD"
    assert Victory("Falcon", "ISD") == "ISD" 

# ----- tally-no -----
    assert Victory("Asteroid", "Asteroid") == "Draw"
    assert Victory("Falcon", "Falcon") == "Draw"
    assert Victory("ISD", "ISD") == "Draw"

# ----- Game play -----
from rockPaperScissors import playRound

def test_playRound_output_validity():
# ----- a list so i can verify manually -----
    valid_outputs = ["Victory is yours", "There's more machine than man here", "Do or do not, there is no tie"]

    for _ in range(50):
        result = playRound("Falcon")
        assert result in valid_outputs

    

