# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates current based on the user inputs.
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------

#-----Import Module -----
import math

#----- Get V and R -----
voltage = int(input("Enter the voltage (in volts): "))
resistance = int(input("Enter the resistance (in ohms): "))

#----- Calc I -----
current = voltage // resistance  # Use integer division unless decimals are allowed

#----- Output -----
print("The current is", current, "amperes.")