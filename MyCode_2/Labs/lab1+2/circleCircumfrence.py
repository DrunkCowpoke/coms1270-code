# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates a Circumfrence based on the user inputs.

# CITATION - URL: # CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------

#-----Import Module -----

import math

#-----Get Rad -----
radius = int(input("Enter the radius of the circle: "))

#-----Calc circumference -----
circumference = 2 * math.pi * radius

#----- Output -----
print("The circumference of the circle is", circumference, "units.")