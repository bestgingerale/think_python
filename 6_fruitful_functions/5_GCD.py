def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


print(gcd(10, 8))
print(gcd(54, 24))
print(gcd(88, 2))
print(gcd(88, 1))
print(gcd(88, 0))
