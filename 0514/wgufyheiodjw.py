import turtle
import datetime
import time

tur = turtle.Turtle()
screen = turtle.Screen()
tur.ht()
tur.speed(0)
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
hour = int(datetime.datetime.now().strftime("%I"))
minute = int(datetime.datetime.now().strftime("%M"))


def drawtime(m, h):
    tur.seth((m * -6 + 90) % 360)
    tur.pendown()
    tur.pensize(2)
    tur.forward(180)
    tur.back(180)
    tur.penup()

    tur.seth((h * -30 + m * -0.5 + 90) % 360)
    tur.pendown()
    tur.pensize(4)
    tur.forward(100)
    tur.back(100)
    tur.penup()


drawtime(minute, hour)


def update():
    global minute
    global hour
    if int(datetime.datetime.now().strftime("%M")) != minute:
        tur.pencolor((1, 1, 1))
        drawtime(minute, hour)
        tur.pencolor((0, 0, 0))
        hour = int(datetime.datetime.now().strftime("%I"))
        minute = int(datetime.datetime.now().strftime("%M"))
        drawtime(minute, hour)
    turtle.ontimer(update, 1000)


turtle.ontimer(update, 1000)
screen.exitonclick()