import turtle

bob = turtle.Turtle()


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

def circle(t, r)
    polygon(t, r, 360)

square(bob, 57.5)
polygon(bob, 50, 66)
circle(bob, 1)

turtle.mainloop()
