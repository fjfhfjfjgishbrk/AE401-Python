import turtle

turt = turtle.Turtle()
turtScreen = turtle.Screen()

turtScreen.title("TURTLE")
turtScreen.bgcolor("red")
turt.color("blue")
turt.shape("turtle")

side = int(input("how many sides: "))

sideCount = 0
while sideCount < side:
    turt.forward(100)
    turt.left(360/side)
    sideCount += 1
