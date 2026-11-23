import turtle
import random
import time

home = turtle.Turtle()
home.shape("circle")
home.color("orange")
home.penup()
home.speed(0)

t = turtle.Turtle()
t.shape('square')
t.color("black")
t.penup()

n_foods = 10
foods_needed = 10
list_of_foods = []
caught = []

bnd = turtle.Turtle()
bnd.ht()
bnd.penup()
bnd.speed(0)
bnd.fillcolor('light green')
bnd.begin_fill()
bnd.goto(-220, -220)
bnd.pendown()
bnd.goto(220, -220)
bnd.goto(220, 220)
bnd.goto(-220, 220)
bnd.goto(-220, -220)
bnd.end_fill()

def make_food():
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)
    caught.append(False)

for kk in range(n_foods):
    make_food()

hawk = turtle.Turtle()
hawk.penup()
hawk.speed(0)
hawk.shape("arrow")
hawk.color("brown")
hawk.shapesize(1.5)
hawk.goto(-200, 200)

hawk_dx = 7
hawk_dy = -5

pen = turtle.Turtle()
pen.penup()
pen.goto(0, 230)
pen.color("black")
pen.ht()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("red")
report.ht()

def right():
    if t.heading() != 180.0:
        t.setheading(0.0)

def left():
    if t.heading() != 0.0:
        t.setheading(180.0)

def up():
    if t.heading() != 270.0:
        t.setheading(90.0)

def down():
    if t.heading() != 90.0:
        t.setheading(270.0)

ts = t.screen
ts.setup(600, 600)
ts.bgcolor("khaki")

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

segments = []
steps = 0
start_time = time.time()
game_over = False

while game_over == False:

    seconds = int(time.time() - start_time)
    pen.clear()
    if len(segments) >= foods_needed:
        message = "Go home or keep eating!  Score: " + str(len(segments)) + "  Time: " + str(seconds) + " s"
    else:
        message = "Score: " + str(len(segments)) + "   Time: " + str(seconds) + " s"
    pen.write(message, align="center", font=("Courier", 16, "normal"))

    for kk in range(len(list_of_foods)):
        if not caught[kk]:
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                list_of_foods[kk].color('green')
                segments.append(list_of_foods[kk])
                make_food()

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(t.xcor(), t.ycor())

    t.forward(20)
    steps = steps + 1

    new_x = hawk.xcor() + hawk_dx
    new_y = hawk.ycor() + hawk_dy
    if abs(new_x) > 200:
        hawk_dx = -hawk_dx
    if abs(new_y) > 200:
        hawk_dy = -hawk_dy
    hawk.setheading(hawk.towards(new_x, new_y))
    hawk.goto(new_x, new_y)

    if abs(t.xcor()) > 210 or abs(t.ycor()) > 210:
        game_over = True
        time.sleep(1)
        report.write("Crashed!!!", align="center", font=("Courier", 24, "normal"))

    elif t.distance(hawk) < 20:
        game_over = True
        report.write("Caught by the hawk!!!", align="center", font=("Courier", 24, "normal"))

    elif len(segments) >= foods_needed and t.distance(home) < 20:
        game_over = True
        time.sleep(1)
        report.write("Back home!\nSteps Taken: " + str(steps), align="center", font=("Courier", 24, "normal"))

    time.sleep(max(0.03, 0.1 - 0.005 * len(segments)))

turtle.done()
