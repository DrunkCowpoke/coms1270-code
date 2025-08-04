# Trevor Bentley                7-2-2025
# 
#lab 4: this code should be a one stop shop for the 4 main files
#  

# ----- Customs Declaration -----

import myOhmsLaw
import myPhysics
import myShapes
import myFinances

# ----- "Home Screen" -----
def main():
    fully_operational = True

    while fully_operational:
        print("Select a Category")
        print("[1] Shapes")
        print("[2] Physics")
        print("[3] Ohm's Law (Phys 2)")
        print("[4] Finances")
        print("[q] Terminate Program")

        choice= input("Your selection: ")

# ----- Shaping Up -----
        if choice == '1':
            print("Shapes selected")
            print("[1a] Rectangle Perimeter")
            print("[1b] Rectangle Area")
            print("[1c] Circumfrence of a Circle")
            print("[1d] Area of a Circle")
            coldsub= input("Pick one: ")

# ----- Shape IF statements -----

            if coldsub == "1a":
                h = int(input("The Length please, good Sir"))
                w = int(input("The Width please, good Sir"))
                print("The Area is:", myShapes.rectanglePerimetere(h,w), ", units are assumed to be decimeters")

            elif coldsub =="1b":
                h = int(input("longness"))
                w = int(input("wideness"))
                print("The Area is:", myShapes.areaOfRectangle(h,w) ,", units are assumed to be decimeters")
            
            elif coldsub == "1c":
                r= int(input("The Radius please"))
                print("Circumfrence", myShapes.circleCircumference(r))

            elif coldsub== "1d":
                r=int(input("Enter the Radius"))
                print("The Area is: ", myShapes.areaOfCircle)

            else:
                print("Try Typing the [] character(s)")

# ----- 2 -----

        elif choice == "2":
            print("Physics Selected")
            print("[2a] Distance")
            print("[2b] Velicity")
            toastedsub= input("Which Option would you like?")
            if toastedsub== "2a":
                s = int(input("What is your speed?"))
                t = int +(input("Time Elapsed"))
                print("Distance Treveled is: ", myPhysics.distanceSpeedTime(s,t))


            elif toastedsub == "2b":
                a = int(input("I'll need your Acceleration"))
                t = int(input("and the time elapsed"))
                print("looks like your Velocity is: ",myPhysics.velocityAccelerationTime(a,t))

            else:
                print("Try Typing the [] character(s)")



        elif choice == "3":
            print("Ohm's Law selected")
            print("[3a] Voltage")
            print("[3b] Resistance")
            print("[3c] Current")
            hoagie= input("Enter your Selection")
            if hoagie =="3a":
                i = int(input("Enter the Current's value."))
                r = int(input("What is the Resistance?"))
                print("the Voltage is: ",myOhmsLaw.calculateVoltage(i,r), "Units are probably Volts")

            elif hoagie == "3b":
                v = int(input("Enter Voltage"))
                i = int(input("whats the Amp draw?"))
                print("ball park for Resistance is: ", myOhmsLaw.calculateResistance(v,i) ,"Units assumed to be Ohms")

            elif hoagie == "3c":
                v = int(input("Voltage Please"))
                r = int(input("Enter the Resistance"))
                print("Current is currently:", myOhmsLaw.calculateCurrent(v,r))


            else:
                print("Try Typing the [] character(s)")

#-----

        elif choice == "4":
            print("Finace selected")
            print()
            print("[4a]Annual Percentage Rate (APR)")
            print("[4b]Compounding Interest")
            print("[4c] Declare Bankruptsy")
            poboy= input("Make your selection")

            if poboy == "4a":
                p= int(input("Just how much money are we talking?"))
                rate= int(input("Whats the interest rate(this is a scary question)"))
                ti= int(input("Whats the Loan Length"))
                fees= int(input("This is where you add on ant ancillary fees"))
                
                print("this APR:", myFinances.annualPercentageRate(rate,fees,p,ti))

            elif poboy =="4b":
                p = int(input("How much would you like to deposit"))
                rate = int(input("What is the rate youre looking at?"))
                tx = int(input("Any idea how many dividends they'll give you?"))
                ti= int(input("and whats the term length youre looing for?"))
                print("Your Compound Interest is:", myFinances.compoundAmount(p,rate,tx,ti))

            elif poboy =="4c":
                print("no Michael, thats not how that works.")

            else:
                print("Try Typing the [] character(s)")


        elif choice == "q":
            print("Until Next Time, this has been the Tonight Show")

        else:
            print("Try Typing the [] character(s)")

if __name__ == "__main__":
    main()

        