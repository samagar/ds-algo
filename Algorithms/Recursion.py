# Algorithm
# Recursion
# Call a function by itself to solve underlying subproblem

'''
Call same function with modified arguments to solve a sub problem
Recursion needs 2 things
Exit Criteria
Function calling same function in loop with modified input (smaller part of input)
'''

# Russian Doll
def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)
openRussianDoll(4)


# Example 2
def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else: 
        recursiveMethod(n-1)
        print(n)
recursiveMethod(4)

# Power of A Number - recursion
# # [0*1*2*...(n-1)]*2
def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
print(powerOfTwo(3))

# Power of Number - Iteration
def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
print(powerOfTwoIt(4))

# Factorial 
# n * (n-1)
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

# Fibonacci 
# (n-1)+(n-2)
def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))