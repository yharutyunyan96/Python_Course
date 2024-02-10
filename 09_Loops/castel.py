import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.title("Castle Drawing")
t = turtle.Turtle()

# Set turtle speed and initial position
t.speed(1)
t.penup()
t.goto(-100, -100)
t.pendown()

# Draw the castle base
t.begin_fill()
t.color("gray")
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Draw the castle towers
t.penup()
t.goto(-40, -100)
t.pendown()
t.begin_fill()
t.color("blue")
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

t.penup()
t.goto(60, -100)
t.pendown()
t.begin_fill()
t.color("blue")
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# Draw the castle roof
t.penup()
t.goto(-120, 0)
t.pendown()
t.begin_fill()
t.color("red")
for _ in range(3):
    t.forward(240)
    t.left(120)
t.end_fill()

# Close the turtle graphics window when clicked
screen.exitonclick()
