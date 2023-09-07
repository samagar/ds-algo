# Problem
# Decimal to Binary

'''
If n == 0 return 0
n%2 + 10 D2b(n/2) recursion
'''
# Question 4 - Decimal to Binary
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))


print(decimalToBinary(1))

