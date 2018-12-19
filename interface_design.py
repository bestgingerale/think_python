import turtle
import math

bob = turtle.Turtle()
alice = turtle.Turtle()

# for i in range(90000):
#     bob.fd(0.05)
#     bob.lt(0.004)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t1, t2, length, n):
    for i in range(n):
        t1.fd(length)
        t1.lt(360/n)
        t2.fd(length)
        t2.rt(360/n)


def circle(t1, t2, r):
    circumference = 2 * math.pi * r
    n = int(circumference/3)+3
    length = circumference / n
    polygon(t1, t2, length, n)


def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


# square(bob, 50)
# square(alice, 60)
# polygon(bob, n=6, length=50)
# circle(bob, alice, 100)
# circle2(bob, 50)
arc(bob, 25, 180)

# print(bob)
# turtle.mainloop()
turtle.exitonclick()
