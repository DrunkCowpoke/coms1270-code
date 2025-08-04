# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculates Velocity based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/physics/learn/patrick/1d-motion-kinematics-new/kinematics-equations
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#-----------------------------------

#----- Import Module -----
import math

#----- Get Velocity and Accel -----
initial_velocity = int(input("Enter the initial velocity (in meters per second): "))
acceleration = int(input("Enter the acceleration (in meters per second squared): "))
time = int(input("Enter the time (in seconds): "))

#----- Calc Velocity -----
final_velocity = initial_velocity + (acceleration * time)

#----- Output -----
print("The final velocity is", final_velocity, "meters per second.")