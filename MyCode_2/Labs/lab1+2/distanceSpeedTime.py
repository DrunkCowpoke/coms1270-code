# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates distance based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/physics/asset/fdf27aef/how-far-has-the-car-traveled-when-it-reaches-60-mph-give-your-answer-both-in-si-?

# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
#----- Import Module -----
import math

#----- Get speed, time -----
speed = int(input("Enter the speed (in meters per second): "))
time = int(input("Enter the time (in seconds): "))

#----- Calc Distance -----
distance = speed * time

#----- Output -----
print("The distance traveled is", distance, "meters.")