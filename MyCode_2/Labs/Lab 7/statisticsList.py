# Trevor Bentley        7-16-2025
# Lab 7 : Statlist

# This code genreates random numbers, then takes the mean and median of said random numbers

import random

def generateInput():
    length = random.randint(200, 500)
    data = []
    for _ in range(length):
        data.append(random.randint(1, 2000))
    return data
# ----- Hulk time -----
def findMean(numList):

    total = 0
    for value in numList:
        total += value
    return total / len(numList)
# ----- i prefer fining medians by turning left ----
def findMedian(numList):
    numList.sort()
    n = len(numList)
    if n % 2 == 1:
        return numList[n // 2]
    else:
        mid1 = numList[n // 2 - 1]
        mid2 = numList[n // 2]
        return (mid1 + mid2) / 2

# ----- Main -----
def main():
    signal = generateInput()
    avg = findMean(signal)
    med = findMedian(signal)
    print("Mean: {:.2f}  Median: {:.2f}".format(avg, med))

if __name__ == "__main__":
    main()