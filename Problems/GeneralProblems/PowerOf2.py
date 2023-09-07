# Problem
# Power of 2


def powerOf2(n):
    if n < 1: return 0
    elif n == 1: return 1

    return 2*powerOf2(int(n/2))

print(powerOf2(50))