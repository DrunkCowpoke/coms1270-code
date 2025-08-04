# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates a circles area based on the user inputs.

# CITATION - URL:# CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------------------------------------

import math

#----- Get Rad -----
radius = int(input("Enter the radius of the circle: "))

#----- Calc Area-----
area = math.pi * (radius ** 2)

#-----Output-----
print("The area of the circle is", area, "square units.")