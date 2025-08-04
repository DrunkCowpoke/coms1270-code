# Trevor Bentley                7-2-2025
# 
#lab 4: this code cab do the main 3 itterations for accel and velocity

#----- Import Module -----
import math

# ----- DST FXN -----
def distanceSpeedTime(s, t):
#----------------------------------------
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------
    return s * t

def main():
    s = int(input("Enter speed: "))
    t = int(input("Enter time: "))
    result = distanceSpeedTime(s, t)
    print("The distance is:", result)

if __name__ == "__main__":
    main()

# ----- VAT FXN -----

def velocityAccelerationTime(v, a, t):
#-----------------------------------
# CITATION - URL: https://www.pearson.com/channels/physics/learn/patrick/1d-motion-kinematics-new/kinematics-equations
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#-----------------------------------
    return v + a * t

def main():
    v = int(input("Enter initial velocity: "))
    a = int(input("Enter acceleration: "))
    t = int(input("Enter time: "))
    result = velocityAccelerationTime(v, a, t)
    print("The final velocity is:", result)

if __name__ == "__main__":
    main()