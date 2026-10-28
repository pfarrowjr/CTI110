#Patrick Farrow
#10/27/2026
#P4Lab1
#Use Turtle and loops to draw a House




import turtle

# Set up the screen and background color
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle House")

# Create the turtle and change its color
pen = turtle.Turtle()
pen.color("darkgreen")
pen.pensize(4)
pen.speed(3)

# Draw the square (house body) using a for loop
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.end_fill()

# Draw the triangle (roof) using a while loop
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()

count = 0
while count < 3:
    pen.forward(200)
    pen.left(120)
    count = count + 1

pen.end_fill()

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()
