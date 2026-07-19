import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.speed(3)

def draw_shape(sides, length, angle, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

draw_shape(3, 100, 120, "#5DCAA5", -200, 0)
draw_shape(4, 100, 90,  "skyblue",  0,    -50)
draw_shape(6, 70,  60,  "orange",   150,  -30)

turtle.done()