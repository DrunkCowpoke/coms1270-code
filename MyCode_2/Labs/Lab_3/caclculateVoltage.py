# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates Voltage amounts based on the user inputs.

#----- Import Module -----
import math

def calculateVoltage(current, resistance):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return current * resistance

def main():
    current = int(input("Enter current: "))
    resistance = int(input("Enter resistance: "))
    result = calculateVoltage(current, resistance)
    print("The voltage is:", result)

if __name__ == "__main__":
    main()
