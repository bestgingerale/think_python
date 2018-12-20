# minutes = 105
#
# hours1 = minutes / 60
# hours2 = minutes // 60
#
# # same thing
# remainder1 = minutes - hours2 * 60
# remainder2 = minutes % 60
#
# print(f'{hours1} hours.')
# print(f'{hours2} hour and {remainder1} minutes.')
# print(f'{hours2} hour and {remainder2} minutes.')


def countdown(n):
    if n < 0:
        print('Done!')
    else:
        print(n)
        countdown(n-1)


def print_n(s, n):
    if n <= 0:
        return
    print(s, n)
    print_n(s, n-1)     # Qs: how come why turns to debug mode, n will increase after turning 0?


def do_n(f, value, num):
    if num <= 0:
        return
    f(value)
    do_n(f, value, num-1)


# countdown(8)
# print_n(2, 5)
do_n(print, value='yes', num=3)
