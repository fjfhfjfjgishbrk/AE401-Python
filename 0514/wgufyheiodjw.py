import turtle
import datetime
import time

tur = turtle.Turtle()
tur2 = turtle.Turtle()
tur3 = turtle.Turtle()
screen = turtle.Screen()
tur.ht()
tur2.ht()
tur3.ht()
tur.speed(0)
tur2.speed(0)
tur3.speed(0)
tur.seth(270)
tur.penup()
tur.forward(220)
tur.pendown()
tur.seth(0)
tur.pensize(3)
tur.circle(220)
tur.pensize(1)
tur.penup()
tur.back(5)
tur.seth(270)
tur.back(210)
tur.seth(60)

for i in range(12):
    tur.forward(200)
    tur.write(i + 1, font=("Arial", 15, "normal"))
    tur.back(200)
    tur.right(30)

tur.seth(90)
tur.forward(13)
tur.seth(0)
tur.forward(4)
tur2.setpos(tur.pos())
tur3.setpos(tur.pos())
hour = int(datetime.datetime.now().strftime("%I"))
minute = int(datetime.datetime.now().strftime("%M"))
second = int(datetime.datetime.now().strftime("%S"))


def drawtime(s, m, h):
    tur.seth((s * -6 + 90) % 360)
    tur.pendown()
    tur.pensize(1)
    tur.forward(180)
    tur.back(180)
    tur.penup()

    tur2.seth((m * -6 + s * -0.1 + 90) % 360)
    tur2.pendown()
    tur2.pensize(2)
    tur2.forward(150)
    tur2.back(150)
    tur2.penup()

    tur3.seth((h * -30 + m * -0.5 + s * -0.0083 + 90) % 360)
    tur3.pendown()
    tur3.pensize(4)
    tur3.forward(80)
    tur3.back(80)
    tur3.penup()


drawtime(second, minute, hour)


def update():
    global minute
    global hour
    global second
    tur.pencolor((1, 1, 1))
    tur2.pencolor((1, 1, 1))
    tur3.pencolor((1, 1, 1))
    drawtime(second, minute, hour)
    tur.pencolor((0, 0, 0))
    tur2.pencolor((0, 0, 0))
    tur3.pencolor((0, 0, 0))
    hour = int(datetime.datetime.now().strftime("%I"))
    minute = int(datetime.datetime.now().strftime("%M"))
    second = int(datetime.datetime.now().strftime("%S"))
    drawtime(second, minute, hour)
    turtle.ontimer(update, 500)


turtle.ontimer(update, 500)
screen.exitonclick()