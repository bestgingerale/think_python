import turtle
import math

bob = turtle.Turtle()
alice = turtle.Turtle()


def square(t, length):
    for j in range(4):
        for i in range(4):
            t.fd(length)
            t.lt(90)
        t.lt(90)


def polygon(t, length, side):
    for j in range(side):
        for i in range(side):
            t.fd(length)
            t.lt(360/side)
        t.lt(360/side)


def circle(t, r):
    for j in range(30):
        circumference = 2 * r * math.pi
        length = circumference/30
        for i in range(30):
            t.fd(length)
            t.lt(360/30)
        t.lt(360/30)


def arc(t, r, angle):
    circumference = 2 * r * math.pi
    length = circumference/30
    for i in range(int(30/360*angle)):
        t.fd(length)
        t.lt(360/30)


# square(bob, length=30)
# polygon(alice, length=19, side=5)
# square(alice, length=30, side=7)
# circle(bob, 50)
arc(bob, 50, 180)
arc(alice, 60, 80)


print(bob)
turtle.mainloop()
