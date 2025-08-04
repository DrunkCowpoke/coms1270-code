# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates resistance based on the user inputs.
 
# CITATION - URL: URL: https://www.pearson.com/channels/physics/learn/patrick/resistors-and-dc-circuits/resistors-ohms-law
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------

#----- Import Module -----
import math

#----- Get V and I -----
voltage = int(input("Enter the voltage (in volts): "))
current = int(input("Enter the current (in amperes): "))

#----- Calc V/I -----
resistance = voltage // current  # Use integer division for now, assuming whole number output

#----- Output -----
print("The resistance is", resistance, "ohms.")