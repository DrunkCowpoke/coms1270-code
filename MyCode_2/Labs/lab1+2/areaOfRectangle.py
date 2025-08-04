# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates a rectangular area based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/calculus/asset/fe1a3253/maximum-area-rectangles-of-all-rectangles-with-a-fixed-perimeter-of-p-which-one-?chapterId=4bf4af9c
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------

#----- Module Import -----
import math

#----- Establishing Variables -----
Base= int(input("Bimenson of Base"))
Height=int(input("Dimension of Height"))

#----- Formula for calc area -----
area= Base * Height

#----- Output -----
print("The Area of the rectangle is", area, "square units")