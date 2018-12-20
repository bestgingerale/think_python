import random


def do_twice(f):
    f()
    f()


def do_twice2(f, arg1, arg2):
    f(arg1)
    f(arg2)


def do_four(f, v):
    do_twice2(f, v, v)
    do_twice2(f, v, v)


def pick_something():
    v = random.randint(1, 100)
    print(v)


def pick_twice(v):
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    print(f'{int1} pairs of {v}')
    print(f'{int2} pairs of {v}')


do_twice(pick_something)
print('\n')
do_twice2(pick_twice, arg1='shoes', arg2='hats')
print('\n')
do_four(print, 'eggs')
