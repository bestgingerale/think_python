import math


def mysqrt(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y


def test_square_root(a):
    print("a", end='   ')
    print("mysqrt(a)".ljust(18), end='  ')
    print("math.sqrt(a)".ljust(18), end='  ')
    print("diff")
    print("-   ---------           ------------        ----")
    for i in range(a):
        i += 1
        j = str(mysqrt(i))
        m = str(math.sqrt(i))
        diff = str(abs(mysqrt(i) - math.sqrt(i)))
        print(float(i), end=' ')
        print(j.ljust(18), end='  ')
        print(m.ljust(18), end='  ')
        print(diff)


print(mysqrt(9))
print()
test_square_root(9)
