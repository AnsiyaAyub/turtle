
import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.setup(400,200)

polygon = turtle.Turtle()
sides = screen.numinput("input window","Enter no of sides: ")
if sides:
    s=int(sides)
    angle = 360//sides

    for i in range(s):
        polygon.forward(50)
        polygon.left(angle)

turtle.done()
