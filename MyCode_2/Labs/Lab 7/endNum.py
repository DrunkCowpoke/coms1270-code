# Trevor Bentley        7-16-2025
# Lab 7 : Number List sorter

# this code takes a target number and pulls all instances of that number and returns it
# A Matrix changer if you will


# ----- Input FXN -----
def getInput():
    result = []
    while True:
        value = input("Enter a number (* to stop): ")
        if value == "*":
            break
        result.append(int(value))
    return result

# ----- the end number do dad -----
def endNum(intList, num):
    notTarget = []
    targets = []

    for value in intList:
        if value == num:
            targets.append(value)
        else:
            notTarget.append(value)

    return notTarget + targets

# ----- for the structure nerds in the crowd -----
def main():
    intList = getInput()
    num = int(input("Enter the number you want to move to the end: "))
    
    shiftedList = endNum(intList, num)
    print("Updated list:", shiftedList)

if __name__ == "__main__":
    main()