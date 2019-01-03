def any_lowercase1(s):
    for c in s:
        if c.islower():  # only checks the first letter
            return True
        return False


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():  # will only return True as it checks "c"
            return 'True'
        return 'False'


def any_lowercase3(s):
    for c in s:
        flag = c.islower()  # will return only the last letter
    return flag


def any_lowercase4(s):
    flag = False
    for c in s:  # correct
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    for c in s:
        if not c.islower():  # checks only the first letter
            return False
    return True


print(any_lowercase4('AppLe'))
print(any_lowercase4('apple'))
print(any_lowercase4('APPLE'))
print(any_lowercase4('applE'))
print(any_lowercase4('APPLEe'))


