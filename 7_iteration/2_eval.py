import math


def eval_loop():
    while True:
        user = input('Please write something.\n')
        if user == 'done':
            break
        a = eval(user)
        print(a)


eval_loop()
