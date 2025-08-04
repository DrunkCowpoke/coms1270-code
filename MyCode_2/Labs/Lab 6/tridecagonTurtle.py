# --------------------------------------------------
# --- UPDATE: UPLOADED TO LAB6 FOLDER FOR TURTLE ---
# --------------------------------------------------

# Trevor Bentley      06-28-2025
# Lab Week 3 - This code creates a tridecagon with a turtle 


import turtle
#----- Function (parent) shape and turtle -----

def tridecagonTurtle(s, x, y, roxanne):
    roxanne.penup()
    roxanne.goto(x, y)
    roxanne.pendown()
    
    for _ in range(13):
        roxanne.forward(s)
        roxanne.left(360 /13)
#----- main function (for organization?) ------
def main():
    s = int(input("Enter side length (s): "))
    x = int(input("Enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    roxanne = turtle.Turtle()

#----- Visability ----- (debugged, defined roxanne after colors, now resides above visability)
    screen = turtle.Screen()
    screen.bgcolor("black")

    roxanne = turtle.Turtle()
    roxanne.color("yellow")
    
    roxanne.pensize(2)
    roxanne.speed(5)
#----- main cont.-----

    tridecagonTurtle(s, x, y, roxanne)

    roxanne.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()