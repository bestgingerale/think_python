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


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 500
    length = int(circumference/n)
    polygon(t, length/500, n)


def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)


def arc(t, r, angle):
    circum = r*2*math.pi
    for i in range(int(circum/360*angle)):
        t.fd(r*2*math.pi)
        t.lt(360/angle)


# square(bob, 50)
# square(alice, 60)
# polygon(bob, n=6, length=50)
# # polygon(bob, 50, 8)
circle(bob, 50)
circle2(bob, 50)
# arc(bob, 25, 180)

# print(bob)
turtle.mainloop()
