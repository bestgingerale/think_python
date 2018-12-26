"""a^n + b^n = c^n"""


def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print('Holy smokes, Fermat was wrong!')
        return
    print("No, that doesn't work.")


def user_input():
    params = {}
    for p in ['a', 'b', 'c', 'n']:
        params[p] = int(input(f'please enter the value of {p}\n'))

    check_fermat(**params)


user_input()
