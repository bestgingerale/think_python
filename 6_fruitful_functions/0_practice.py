# x^2 + y^2 = z^2
# distance = 	√(x2 − x1)^2 + (y2 − y1)^2
import math


def area(radius):
    return math.pi * radius**2


def distance(x1, y1, x2, y2):
    dx2 = (x2-x1) ** 2
    dy2 = (y2-y1) ** 2
    z = math.sqrt(dy2+dx2)
    return z


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp)/2)


print(distance(1, 2, 4, 6))
print(circle_area(1, 2, 4, 6))


# x = int(input('x='))
# y = int(input('y='))


def is_divisible(a, b):
    return a % b == 0


# if is_divisible(x, y):
#     print('Yes, divisible.')
# else:
#     print('Nope, not divisible.')


def is_between(x, y, z):
    return x <= y <= z


print(is_between(3, 6, 100))
print(is_between(3, 6, 5))


def factorial(n):
    space = "x" * n
    print(space, "factorial", n)
    if not isinstance(n, int):
        print('Has to be an integer.')
    elif n < 0:
        print('Has to be positive.')
    elif n == 0:
        return 1
    result = n * factorial(n-1)
    print(space, "factorial", n)
    return result


print(factorial(3))
# a = int(input('Please enter:\n'))
# print(factorial(a))
