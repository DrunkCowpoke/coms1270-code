# Trevor Bentley                7-2-2025
# 
#lab 4: This code runs some elementry geometry calculations


#-----Import Module -----

import math

# ----- Circle Area FXN -----

def areaOfCircle(r):

#--------------------------------------------------------------------------------
# CITATION - URL:# CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------------------------------------
    return 3.14159 * r ** 2

def main():
    r = int(input("Enter radius: "))
    result = areaOfCircle(r)
    print("The area of the circle is:", result)

if __name__ == "__main__":
    main()

# ----- Circumfrence FXN -----

def circleCircumference(r):
#----------------------------------------
# CITATION - URL: # CITATION - URL: https://www.pearson.com/channels/calculus/asset/c9f6c203/functions-and-graphsexpress-the-area-and-circumference-of-a-circle-as-functions-?chapterId=604ca5b4
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return 2 * 3.14159 * r

def main():
    r = int(input("Enter radius: "))
    result = circleCircumference(r)
    print("The circumference of the circle is:", result)

if __name__ == "__main__":
    main()

# ----- Rectangle Area FXN -----

def areaOfRectangle(w, h):
#----------------------------------------
# CITATION - URL: https://www.pearson.com/channels/calculus/asset/fe1a3253/maximum-area-rectangles-of-all-rectangles-with-a-fixed-perimeter-of-p-which-one-?chapterId=4bf4af9c
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return w * h

def main():
    w = int(input("Enter width: "))
    h = int(input("Enter height: "))
    result = areaOfRectangle(w, h)
    print("The area of the rectangle is:", result)

if __name__ == "__main__":
    main()

# ----- Rectangle Perimeter FXN -----

def rectanglePerimeter(w, h):
#----------------------------------------
# CITATION - URL: https://www.pearson.com/channels/calculus/asset/fe1a3253/maximum-area-rectangles-of-all-rectangles-with-a-fixed-perimeter-of-p-which-one-?chapterId=4bf4af9c
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025‑06‑28
#----------------------------------------
    return 2 * (w + h)

def main():
    w = int(input("Enter width: "))
    h = int(input("Enter height: "))
    result = rectanglePerimeter(w, h)
    print("The perimeter of the rectangle is:", result)

if __name__ == "__main__":
    main()