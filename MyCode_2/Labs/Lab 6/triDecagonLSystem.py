# Name: Trevor Bentley      7-9-2025
# Lab 6: Strings and things

# this code turtles 

# ----- Importing Modules -----
import turtle
import random

#----- Lazy Import (Yes I copied it into the directory) ----
import tridecagonTurtle

# ----- FXN for upgrade -----
def fixit(ch):
    if ch == 'f':
        return "F-H+FP+F+H-F"
    else:
        return ch

# ----- String Evaluation -----
def evalstring(oldStr):
    newStr = ""
    for ch in oldStr:
        newStr += fixit(ch)
    return newStr

# ----- the L-Sys "frame" -----
def lsys(iters,axiom):
        result = axiom
        for _ in range(iters):
            result = evalstring(result)
        return result

# ----- Command Changes -----
def command(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == 'H':
            tridecagonTurtle.turtleyBoi(t, 30)
        elif cmd == 'P':
            t.penup()
            t.goto(random.randint(-200, 200), random.randint(-200, 200))
            t.pendown()

#----- main FXN ----
def main():
    wn = turtle.Screen()
    wn.bgcolor("midnightblue")
# ----- we had some issues in the raw import so -----
    roxanne = turtle.Turtle()
    roxanne.color("red")
    roxanne.pensize(2)
    roxanne.speed(0)

    axiom = "f"
    instructions = lsys(3, axiom)

    print("Instructions:", instructions)

    lsys(roxanne, instructions, 75, 10)

    wn.exitonclick()

# ----- Cue Porky Pig -----
if __name__ == "__main__":
    main()