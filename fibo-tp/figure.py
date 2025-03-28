import turtle
from math import *

# Turtle setup
t = turtle.Turtle()
s = turtle.Screen()
t.speed(100)

def draw_circle(turtle:turtle.Turtle, screen:turtle.Screen, color:str="yellow", radius:int = 50):
    # Draws a full yellow circle
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_square(turtle:turtle.Turtle, screen:turtle.Screen, color:str="red", side:int = 50):
    # Draws a full red square
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def draw_trapezoid(turtle:turtle.Turtle, screen:turtle.Screen, base:int, top:int, height:int, color:str="green"):

    # Finds base of the triangle for angle calculations
     # Devides by 2 to get half the remaining side length
    if base > top: triangle_base = (base - top) / 2
    elif top > base: triangle_base = (top - base) / 2
    else: raise NotImplementedError("Error calculating base of triangle for trapezoid angle caluclations")

    # Finds side length of the triangle: sqrt(a^2 + b^2 - 2ab * cos(C)) with C = 0 so 2ab * cos(0) = 0
    side = sqrt(
        pow(height, 2) + pow(triangle_base, 2)
        )

    # Finds angle of the triangle: acos((a^2 + b^2 - c^2) / 2ac)
    angle = degrees(
        acos(
            ( pow(side, 2) + pow(triangle_base, 2) - pow(height, 2) ) / ( 2 * side * triangle_base )
        )
    )

    # Draws the trapezoid
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()


    # Draws base & first side
    turtle.forward(base)
    turtle.left(180 - angle)
    turtle.forward(side)

    # Draws top & second side
    turtle.left(angle)
    turtle.forward(top)
    turtle.left(angle)
    turtle.forward(side)

    turtle.end_fill()

def goto(turtle:turtle.Turtle, x:int, y:int):
    # Moves the turtle to a specific location
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Draws square
goto(t, -50, -50)
draw_square(t, s, "red", 100)

# Draws circles
goto(t, -20, -30)
draw_circle(t, s, "yellow", 20)
goto(t, 20, -30)
draw_circle(t, s, "yellow", 20)

# Draws trapezoid, x = origin - 1/2 base, y = origin - 1/2 square - height
goto(t, -100, -170)
draw_trapezoid(t, s, 200, 80, 120, "green")


turtle.done()
input("Press enter to exit...")