from curses import window
from turtle import Screen, Turtle

def draw(turtle):
    turtle.speed(0)
    turtle.hideturtle()
    for i in range(2000):
        turtle.forward(4 + i**0.98)
        turtle.left(91)

window = Screen()
turtle = Turtle()

draw(turtle)

window.exitonclick()
