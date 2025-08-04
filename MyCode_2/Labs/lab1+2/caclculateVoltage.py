# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates Voltage amounts based on the user inputs.

# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------

#----- Import Module -----
import math

#----- Get A and R -----
current = int(input("Enter the current (in amperes): "))
resistance = int(input("Enter the resistance (in ohms): "))

#----- Calc Voltage -----
voltage = current * resistance

# -----Output -----
print("The voltage is", voltage, "volts.")