# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculates Velocity based on the user inputs.

#----- Import Module -----
import math

def velocityAccelerationTime(initial_velocity, acceleration, time):
#-----------------------------------
# CITATION - URL: https://www.pearson.com/channels/physics/learn/patrick/1d-motion-kinematics-new/kinematics-equations
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#-----------------------------------
    return initial_velocity + acceleration * time

def main():
    initial_velocity = int(input("Enter initial velocity: "))
    acceleration = int(input("Enter acceleration: "))
    time = int(input("Enter time: "))
    result = velocityAccelerationTime(initial_velocity, acceleration, time)
    print("The final velocity is:", result)

if __name__ == "__main__":
    main()
