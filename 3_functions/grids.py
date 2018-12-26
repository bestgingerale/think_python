def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def plus():
    print('+ ', end='')


def minus():
    print('- ', end='')


def slash():
    print('/ ', end='')


def space():
    print('  ', end='')


def plus_minus():
    plus()
    do_four(minus)


def plus_minus_line():
    # do_twice(plus_minus)    # two by two
    do_four(plus_minus)   # four by four
    plus()


def slash_space():
    slash()
    do_four(space)


def slash_space_line():
    # do_twice(slash_space)   # two by two
    do_four(slash_space)  # four by four
    slash()
    print('\t')


def hat():
    plus_minus_line()
    print('\t')
    do_four(slash_space_line)


def grids():
    # do_twice(hat)   # two by two
    do_four(hat)  # four by four
    plus_minus_line()
    print()


# plus_minus()
# plus_minus_line()
# hat()
do_twice(grids)
