def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# print(first(' '))
# print(last(' '))
# print(middle(' '))


def is_palindrome(m):
    if len(m) != len(m):
        return False
    elif first(m) != last(m):
        return False
    elif is_palindrome(middle(m)) != is_palindrome(middle(m)):
        return False
    return True


print(is_palindrome('noon'))
