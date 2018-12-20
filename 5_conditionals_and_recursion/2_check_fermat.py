"""a^n + b^n = c^n"""


def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print('Holy smokes, Fermat was wrong!')
        return
    print("No, that doesn't work.")


a1 = int(input('a = '))
b2 = int(input('b = '))
c3 = int(input('c = '))
n4 = int(input('n = '))
check_fermat(a1, b2, c3, n4)
