# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates a circles area based on the user inputs.


import math

def areaOfCircle(radius):
#--------------------------------------------------------------------------------
# CITATION - URL:# CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------------------------------------
    return 3.14159 * radius ** 2

def main():
    radius = int(input("Enter radius: "))
    result = areaOfCircle(radius)
    print("The area of the circle is:", result)

if __name__ == "__main__":
    main()
