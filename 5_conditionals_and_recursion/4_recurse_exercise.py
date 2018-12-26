"""
By default sum should equal to 0,
this function calculates the sum from 0 to n.
"""


def recurse(n, s, i=0):
    print(i)
    if n == 0:
        print(s)
    else:

        recurse(n-1, n+s, i+1)
    print(i)
    # print(f'recurse number {i} ended')


recurse(3, 0)
# recurse(5, 0)
# recurse(100, 0)
print('\n')


def total(n):
    s = 0
    for i in range(n+1):
        s += i
    print(s)


# total(3)
# total(5)
# total(10)

