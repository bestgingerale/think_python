def ack(m, n):
    if m == 0:
        # print(n+1)
        return n+1
    elif m > 0 and n == 0:
        # print(m-1, 1)
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        # print(m-1, m, n-1)
        return ack(m-1, ack(m, n-1))


print(ack(3, 4))
