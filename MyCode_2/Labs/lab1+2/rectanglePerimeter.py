# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates a rectangular perimeter based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/calculus/asset/fe1a3253/maximum-area-rectangles-of-all-rectangles-with-a-fixed-perimeter-of-p-which-one-?chapterId=4bf4af9c
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025‑06‑28
#----------------------------------------

#----- Import Module -----
import math

#----- Ask user for length and width -----
Length = int(input("Enter the length of the rectangle: "))
Width = int(input("Enter the width of the rectangle: "))

#----- Perimeter Calc -----
Perimeter = 2 * (Length + Width)

#----- Output -----
print("The perimeter of the rectangle is", Perimeter, "units.")