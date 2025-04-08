import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("Midnight Blue")

t.color("navy")

t.penup()
t.goto(0, 0)
t.pendown()
t.color("light blue")
t.speed(10)

for i in range (100) :
    t.forward(200 + i)
    t.left(170)
    t.forward(260 + i)
    t.left(177)

t.penup()

t.goto(-100, -100)
t.pendown()
t.color("orange")
t.speed(10)

for i in range (100) :
    t.forward(200 + i)
    t.left(170)
    t.forward(260 + i)
    t.left(177)

t.penup()

t.goto(-120, -80)
t.pendown()
t.color("white")
t.speed(10)

for i in range (100) :
    t.forward(200 + i)
    t.left(170)
    t.forward(260 + i)
    t.left(177)

turtle.exitonclick() 