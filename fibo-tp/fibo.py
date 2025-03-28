# Imports
import turtle

def fibo(end=None, start=0, inclusive=True, length=None):
    fibonacci_list = []

    start = int(start) + 1 if start > int(start) else int(start)

    if end:
        # Defines an end number with optional start and inclusive args.
        end = int(end) if inclusive else int(end)-1
        a, b = (0, 1) if start == 0 else (start, start)

        # Computes fibonacci until end is reached
        while a <= end:
            fibonacci_list.append(a)
            a, b = b, b + a

    if length:
        # Defines the length of the series list by using length argument with optional start argument.
        a, b = (0, 1) if start == 0 else (start, start)

        # Computes fibonacci until len(fibonacci_list) reaches the length
        for _ in range(length):
            fibonacci_list.append(a)
            a, b = b, b+a

    return fibonacci_list

# Turtle setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

# Turtle start settings
t.color("white")
t.pensize(2)
t.speed(0)
t.penup()
t.goto(-200, 200)
t.pendown()
fibolist = fibo(int(input("Enter the maximum number for the fibonacci sequence: ")))

# Draw
for i in range(fibolist.__len__()):
    t.circle(fibolist[i], extent=45)

input("Press enter to exit...")