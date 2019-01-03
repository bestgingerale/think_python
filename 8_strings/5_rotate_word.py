to_be_code = {'A': 3,
              'Z': 1,
              'cheer': 7,
              'melon': -10,
              'HAL': 1,
              'mElOn': -10,
              'Uryyb Jbeyq!': 13
              }


def rotate_word(s, n):
    res = ''
    piece = list(s)
    for i in piece:
        if i.islower():
            c = ord(i) + n
            if ord('a') <= c <= ord('z'):
                res += chr(c)
            elif c > ord('z'):
                new = c - 26 * ((c - 123) // 26 + 1)
                res += chr(new)
            elif c < ord('a'):
                new = c + 26 * ((96 - c) // 26 + 1)
                res += chr(new)
        elif i.isupper():
            c = ord(i) + n
            if ord('A') <= c <= ord('Z'):
                res += chr(c)
            elif c > ord('Z'):
                new = c - 26 * ((c - 91) // 26 + 1)
                res += chr(new)
            elif c < ord('A'):
                new = c + 26 * ((64 - c) // 26 + 1)
                res += chr(new)
        else:
            res += i
    return res


def exercise():
    for k, v in to_be_code.items():
        print(rotate_word(k, v))


exercise()

# def bug():
#     print('\nDebugging:')
#     print(rotate_word('melon', -10))
#     print(rotate_word('HAL', 1))
#     print(rotate_word('HAL', 27))


# bug()


# draft
# def rotate_word(s, number):
#     n = ''
#     if s.islower():
#         for x in s:
#             code = ord(x) + number
#             if 97 <= code <= 122:
#                 n += chr(code)
#             elif code > 122:
#                 code_adjusted = code - 26 * ((int((code - 123) / 26)) + 1)
#                 n += chr(code_adjusted)
#             elif code < 97:
#                 code_adjusted = code + 26 * int((96 - code) / 26 + 1)
#                 n += chr(code_adjusted)
#     elif s.isupper():
#         for x in s:
#             code = ord(x) + number
#             if 65 <= code <= 90:
#                 n += chr(code)
#             elif code > 90:
#                 code_adjusted = code - 26 * ((int((code - 91) / 26)) + 1)
#                 n += chr(code_adjusted)
#             elif code < 65:
#                 code_adjusted = code + 26 * (int((64 - code) / 26) + 1)
#                 n += chr(code_adjusted)
#     elif any_uppercase(s):
#         piece = list(s)
#         for i in piece:
#             if i.islower():
#                 code = ord(i) + number
#                 if 97 <= code <= 122:
#                     n += chr(code)
#                 elif code > 122:
#                     code_adjusted = code - 26 * ((int((code - 123) / 26)) + 1)
#                     n += chr(code_adjusted)
#                 elif code < 97:
#                     code_adjusted = code + 26 * int((96 - code) / 26 + 1)
#                     n += chr(code_adjusted)
#             elif i.isupper():
#                 code = ord(i) + number
#                 if 65 <= code <= 90:
#                     n += chr(code)
#                 elif code > 90:
#                     code_adjusted = code - 26 * ((int((code - 91) / 26)) + 1)
#                     n += chr(code_adjusted)
#                 elif code < 65:
#                     code_adjusted = code + 26 * (int((64 - code) / 26) + 1)
#                     n += chr(code_adjusted)
#     return n
