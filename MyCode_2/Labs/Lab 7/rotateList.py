# Trevor Bentley        7-16-2025
# Lab 7 : roto list

# this code takes an input and rotates, + to right, - to left, 0 stays the same

# --- input -----
def getInput():
    numbers = []
    while True:
        value = input("Enter a number (* to stop): ")
        if value == "*":
            break
        numbers.append(int(value))
    return numbers

 # ----- Roto-rooter -----
def rotateList(intList, rot):
    n = len(intList)
    if n == 0:
        return intList

    rot = -rot % n 
    return intList[rot:] + intList[:rot]
# ----- Main FXN -----
def main():
    intList = getInput()
    rot = int(input("Enter a rotation amount (positive = right, negative = left, 0 = 0): "))
    
    rotated = rotateList(intList, rot)
    print("Rotated list:", rotated)

if __name__ == "__main__":
    main()