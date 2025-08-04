# Trevor Bentley            7-2-2025
# Lab 4: this code draws custom tridecagons

# ----- Imported Modules -----
import turtle
import math

#----- Function (parent) shape and turtle -----

def tridecagonTurtle(s, x, y, roxanne):
    roxanne.penup()
    roxanne.goto(x, y)
    roxanne.pendown()
    
    for _ in range(13):
        roxanne.forward(s)
        roxanne.left(360 /13)

# ----- Multiples -----

def drawMultipleTridecagonTurtle(s,x,y,no,sr,roxanne):
    for i in range(no):
        x2= x+i*sr
        tridecagonTurtle(s,x2,y,roxanne)

#----- Main Function ------
def main():
    s = int(input("Enter side length (s): "))
    x = int(input("Enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    no = int(input("How many Tridecagons?"))
    sr = int(input("Spacing between each: "))



#----- Visability ----- (debugged, defined roxanne after colors, now resides above visability)
    screen = turtle.Screen()
    screen.bgcolor("black")

    roxanne = turtle.Turtle()
    roxanne.color("yellow")
    
    roxanne.pensize(2)
    roxanne.speed(5)


#----- main cont.-----

    drawMultipleTridecagonTurtle(s, x, y,no,sr, roxanne)

    roxanne.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()