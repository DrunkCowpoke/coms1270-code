# Trevor Bentley      06-28-2025
# Lab Week 2 - This code turtles out my initials
#------------------------------

#----- Module Import -----
import turtle 

#----- Screen defaults -----
screen = turtle.Screen()
screen.bgcolor("lightgrey")

#----- Turtle defaults -----
pen=turtle.Turtle()
pen.pensize(5)
pen.speed(5)

#----- T-ing off -----
pen.penup()

pen.goto(-150, 0) 
pen.pendown()

pen.color("Blue","green")
pen.begin_fill()

#----- t-structure -----
pen.forward(100)
pen.backward(50)
pen.right(90)
pen.forward(150)
#-------------------------

#----- B intililizing -----
pen.penup()
pen.goto(0,-75)

pen.pendown()

#----- Changing pen defaults for B -----
pen.color("orange","Yellow")
pen.begin_fill()

#----- B shape -----
pen.forward(75)
pen.backward(150)

pen.left(90)
pen.forward(40)

pen.circle(-40, 180)
pen.forward(40)
pen.backward(50)
pen.circle(40,-180)
pen.backward(50)
pen.end_fill()



#----- Termination -----
pen.hideturtle() #turns out the hide function exists
screen.exitonclick()