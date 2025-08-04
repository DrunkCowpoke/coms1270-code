# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates a Circumfrence based on the user inputs.


#-----Import Module -----

import math

def circleCircumference(radius):
    #----------------------------------------
# CITATION - URL: # CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return 2 * 3.14159 * radius

def main():
    radius = int(input("Enter radius: "))
    result = circleCircumference(radius)
    print("The circumference of the circle is:", result)

if __name__ == "__main__":
    main()
