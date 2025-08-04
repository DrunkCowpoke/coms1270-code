# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates resistance based on the user inputs.


#----- Import Module -----
import math

def calculateResistance(voltage, current):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return voltage // current

def main():
    voltage = int(input("Enter voltage: "))
    current = int(input("Enter current: "))
    result = calculateResistance(voltage, current)
    print("The resistance is:", result)

if __name__ == "__main__":
    main()
