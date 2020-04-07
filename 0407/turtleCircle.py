import turtle

turt = turtle.Turtle()

turt.shape("turtle")
turt.color("brown")
turt.penup()

for i in range(30):
    turt.forward(5+3*i)
    turt.right(30)
    turt.stamp()
