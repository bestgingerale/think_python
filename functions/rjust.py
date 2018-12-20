def right_justify(v, l, f):
    space = l - len(v)
    print(space * f + v)


right_justify('yes', 30, '-')
right_justify('no', 30, '*')
right_justify('hello world!', 30, '+')


# The built-in rjust()

print('happy'.rjust(30, '-'))
print('sad'.ljust(30, '-'))
print('excited'.center(30, '-'))
