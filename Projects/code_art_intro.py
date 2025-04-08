# ###################################
# ############## SETUP ##############
import turtle
# ###################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

t = turtle.Turtle()
t.penup()
t.goto(-100, 50)
t.color("yellow")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

t = turtle.Turtle()
t.penup()
t.goto(-100, 200)
t.color("blue")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

t = turtle.Turtle()
t.penup()
t.goto(-250, -100)
t.color("pink")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

t = turtle.Turtle()
t.penup()
t.goto(-250, 50)
t.color("yellow")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

t = turtle.Turtle()
t.penup()
t.goto(-250, 200)
t.color("blue")
t.pendown()

# repeat these next two lines 4 times
for i in range(4):
    t.forward(100)
    t.left(90)

# ###################################
# ############## ENDING ##############
turtle.exitonclick()
# ###################################