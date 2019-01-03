def is_palindrome(a):
    if a == a[::-1]:
        return True
    return False


print(is_palindrome('banana'))
print(is_palindrome('yesey'))
