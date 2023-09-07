# Problem
# Greatest Common Divisor

''''

Eucledian Algorithm
gcd(48,12)
48/18 - 2 reminder 12
18/12 - 1 reminder 6
12/6 - 2  reminder 0

recursive function >> gcd(b, a%b)
stop condition b==0 return a

'''

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(12,1.2))