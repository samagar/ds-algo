# Problem
# Solve Fibonacci using Top down & bottom up approach

def fibonacciTopDown(n, memo):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1

    if not n in memo:
        memo[n] = fibonacciTopDown(n-1, memo) + fibonacciTopDown(n-2, memo)
    return memo[n]

def fibonacciBottomUp(n):
    tb = [0,1]
    for i in range(2, n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n]


# Driver Code
myDict = {}
print(fibonacciTopDown(9, myDict))
print(fibonacciBottomUp(9))


''' Fibonacci without dynamic programming '''

def fib(n):
    if n in [0,1]: return n
    else: return fib(n-1) + fib(n-2)

print(fib(9))
