# Problem
# Factorial 


def factorial(n, dict):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]: return 1
    elif n not in dict:
        dict[n] = n * factorial(n-1, dict)

    return dict[n]

myDict = {}
print(factorial(10,myDict))