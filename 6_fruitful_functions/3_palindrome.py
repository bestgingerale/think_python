def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# print(first(' '))
# print(last(' '))
# print(middle(' '))


# def is_palindrome(m):
#     if first(m) != last(m):
#         return False
#     elif first(middle(m)) != last(middle(m)):
#         return False
#     return True


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('abccba'))

