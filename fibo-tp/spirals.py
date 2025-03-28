# Imports
import turtle

def squareals():
    # Turtle setup
    t1 = turtle.Turtle()

    t1.speed(1000)
    t1.penup()
    t1.goto(0, 0)
    t1.pendown()
    t1.color("blue")
    t1.right(90)

    # Draw
    for i in range(100):
        t1.forward(10 * i)
        t1.right(90)

def spirals():
    t2 = turtle.Turtle()

    t2.speed(1000)
    t2.penup()
    t2.goto(0, 0)
    t2.pendown()
    t2.color("red")
    t2.right(90)

    # Draw
    for i in range(360 * 3):
        t2.forward(i * 0.1)
        t2.right(10)

squareals()
spirals()