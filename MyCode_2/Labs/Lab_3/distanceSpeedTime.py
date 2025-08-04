# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates distance based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/physics/asset/fdf27aef/how-far-has-the-car-traveled-when-it-reaches-60-mph-give-your-answer-both-in-si-?

#----- Import Module -----
import math

def distanceSpeedTime(speed, time):
#----------------------------------------
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return speed * time

def main():
    speed = int(input("Enter speed: "))
    time = int(input("Enter time: "))
    result = distanceSpeedTime(speed, time)
    print("The distance is:", result)

if __name__ == "__main__":
    main()
