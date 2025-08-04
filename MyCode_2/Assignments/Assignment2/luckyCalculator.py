# Trevor Bentley        7-1-2025
#Assignment #2:Lucky Calc

#This code lets the useer perfom basic math ops
#This code also generates a lucky number
#You still cant div by 0, but it wont crash.
#-----------------------------------------------

# ----- Importing the Random Module -----
import random
#Importing a flourish
#CITATION: https://docs.python.org/3/tutorial/modules.html#tut-standardmodules
import time

# ----- The Begining of a Header Function ------

def print_header():
    print("Lucky Calculator")
    print("by: Trevor Bentley")
    print("I did have fun with this one")
    print("[COM S 1270 A]")
    print()
    
# ----- The Big Conditional function ft. tri-nesting -----
print_header()

print("What are we doing this time?")
print("[1] Calculator")
print("[2] Lucky Number")
print("[3] Quit")

ui = input("Choose: ").lower()

# ------ Calculator fxn -----
if ui == "1" or ui == "c":
    co= input("Pleae choose an operator [-],[+],[*],[/],[//],[%],[**]")
    if co not in['+','-','*','/','//','%','**']:
        print("... okay but what if we choose one of the options..."
              "These are the options: [+], [-], [*], [/], [//], [%], [**]")

    a=int(input("Please enter an Integer"))
    b=int(input("Please enter another Integer"))
#----- The Zeroing -----
#----- Yes This took a second -----
    if b==0 and co in ["/","//","%"]:
        time.sleep(2)
        print("...")
        print("Yeah I'm not doing L'Hoptital: b=0")
        time.sleep(2)
        print("...")
        print("  (o_0 )")
        print("  /|_|--(?)")
        print("   _/ \\_ ")
        print("   |/. ")
        print("let's try again.")
        b= 1

    if co == "+":
            result = a + b
    elif co == "-":
            result = a - b
    elif co == "*":
            result = a * b
    elif co == "/":
            result = a / b
    elif co == "//":
            result = a // b
    elif co == "%":
            result = a % b
    elif co == "**":
        result = a ** b

    print("According to my calculations:", result, "is your answer.")

elif ui== "2" or ui == "l":
    minimum= int(input("Please enter an integer"))
    maximum= int(input("Please enter an integer"))
    missingno= random.randint(minimum,maximum)

    print("The odds of surviving that calculation are", missingno ,"to one.")
    time.sleep(2)
    print("Just in case your Lucky Number is", missingno ,".")


elif ui == "3" or ui== "q":
    print("Farewell...")
    time.sleep(2)
    print("May the Force be with you.")

# ----- Bad feelings -----
else:
    print("You have another target? A Military Target?")
    print("Then Fix your input.")