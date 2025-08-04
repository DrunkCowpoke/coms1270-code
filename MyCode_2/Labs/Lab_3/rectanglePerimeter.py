# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates a rectangular perimeter based on the user inputs.

def rectanglePerimeter(width, height):
#----------------------------------------
# CITATION - URL: https://www.pearson.com/channels/calculus/asset/fe1a3253/maximum-area-rectangles-of-all-rectangles-with-a-fixed-perimeter-of-p-which-one-?chapterId=4bf4af9c
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025‑06‑28
#----------------------------------------
    return 2 * (width + height)

def main():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    result = rectanglePerimeter(width, height)
    print("The perimeter of the rectangle is:", result)

if __name__ == "__main__":
    main()
