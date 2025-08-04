# Trevor Bentley                7-2-2025
# 
#lab 4: This code can do the 3 main Ohms law calculations 


#----- Import Module -----

import math

# ----- Voltage FXN -----
def calculateVoltage(c, r):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return c * r

def main():
    c = int(input("Enter current: "))
    r = int(input("Enter resistance: "))
    result = calculateVoltage(c, r)
    print("The voltage is:", result)

if __name__ == "__main__":
    main()

# ----- Resistance FXN -----

def calculateResistance(v, c):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return v // c

def main():
    v = int(input("Enter voltage: "))
    c = int(input("Enter current: "))
    result = calculateResistance(v, c)
    print("The resistance is:", result)

if __name__ == "__main__":
    main()

# ----- Current FXN -----

def calculateCurrent(v, r):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return v // r

def main():
    v = int(input("Enter voltage: "))
    r = int(input("Enter resistance: "))
    result = calculateCurrent(v, r)
    print("The current is:", result)

if __name__ == "__main__":
    main()
