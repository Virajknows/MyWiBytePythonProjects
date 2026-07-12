import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)


def jump_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(x, y, width, height, fill, pen):
    jump_to(x, y)
    t.pencolor(pen)
    t.fillcolor(fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def sun():
    jump_to(220, 180)
    t.pensize(3)
    t.pencolor("orange")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


def cloud(x, y):
    jump_to(x, y)
    t.dot(45, "white")
    jump_to(x + 30, y + 10)
    t.dot(55, "white")
    jump_to(x + 65, y)
    t.dot(45, "white")


def rainbow():
    colours = ["red", "orange", "green", "purple"]
    radius = 160
    t.pensize(8)
    for c in colours:
        jump_to(-250 + (160 - radius), 50)
        t.pencolor(c)
        t.setheading(90)
        t.circle(-radius, 180)
        radius -= 12
    t.setheading(0)


def house():
    rectangle(-60, -150, 160, 110, "lightcoral", "black")
    rectangle(-10, -150, 40, 60, "saddlebrown", "black")
    jump_to(-70, -40)
    t.pencolor("black")
    t.fillcolor("firebrick")
    t.begin_fill()
    t.forward(180)
    t.left(120)
    t.forward(180)
    t.left(120)
    t.forward(180)
    t.end_fill()
    t.setheading(0)


def flower(x, y, petal_colour):
    t.pensize(2)
    jump_to(x, y)
    t.pencolor("darkgreen")
    t.setheading(90)
    t.forward(35)
    t.pencolor(petal_colour)
    t.fillcolor(petal_colour)
    for _ in range(6):
        t.begin_fill()
        t.circle(8)
        t.end_fill()
        t.left(60)
    t.dot(10, "gold")
    t.setheading(0)


def grass():
    rectangle(-400, -300, 800, 130, "lawngreen", "lawngreen")


grass()
sun()
cloud(-120, 180)
cloud(60, 210)
rainbow()
house()

flower(-150, -170, "hotpink")
flower(120, -180, "mediumpurple")
flower(180, -160, "deeppink")

t.hideturtle()
turtle.done()
