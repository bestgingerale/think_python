def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('No')
        return
    print('Yes')


a1 = input()
a2 = input()
a3 = input()

is_triangle(a1, a2, a3)
