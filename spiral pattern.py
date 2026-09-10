import turtle

turtle.Screen().bgcolor("Light Blue")
turtle.Screen().title("Turtle")

draw = turtle.Turtle()

size = 0

while True:
    for i in range(4):
        draw.forward(size + 1)
        draw.left(90)
        size -= 5
    size += 1