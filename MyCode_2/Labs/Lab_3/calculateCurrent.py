# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates current based on the user inputs.

#-----Import Module -----
import math

def calculateCurrent(voltage, resistance):
#----------------------------------------
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return voltage // resistance

def main():
    voltage = int(input("Enter voltage: "))
    resistance = int(input("Enter resistance: "))
    result = calculateCurrent(voltage, resistance)
    print("The current is:", result)

if __name__ == "__main__":
    main()
