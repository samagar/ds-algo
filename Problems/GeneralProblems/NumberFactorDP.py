# Problem
# Find number of ways N can be expressed as sum of 1, 3 & 4
# Divide and conquer

'''
N can be expressed as: f(N-1)+1, f(N-3)+3 & f(N-4)+4 in terms of 1,3,4
N-3 = number of times N can be expressed as 3 and so for 1 & 4

For N=0,1,2 - It can expressed as 1
For 3 it can expressed as 2
Else sum(func for N-3,N-1, & N-4)

'''

# Basic devide and conquer 
def numFact(n):
    if n in (0,1,2): return 1
    elif n==3: return 2
    else:
        func1 = numFact(n-1)
        func3 = numFact(n-3)
        func4 = numFact(n-4)
        return func1 + func3 + func4

N = 5
print("Number factorial of {} in terms of 1,3,4 is".format(N))
print(numFact(N))


# Top Down Approach
def numFactTD(n, TDdict):
    if n in (0,1,2): return 1
    if n is 3: return 2
    elif n in TDdict: return TDdict[n]
    else:
        func1 = numFactTD(n-1, TDdict)
        func3 = numFactTD(n-3, TDdict)
        func4 = numFactTD(n-4, TDdict)
        TDdict[n] = func1 + func3 + func4
        return TDdict[n]

# Driver code
TDdict = {}
print("Top Down Number factorial of {} in terms of 1,3,4 is".format(N))
print(numFactTD(N, TDdict))        

# Bottom Up Approach'''
def numFactBU(n):
    factList = [1,1,1,2]

    for i in range(4, n+1):
        factList.append(factList[i-1]+factList[i-3]+factList[i-4])
    return factList[n]

# Driver code
print("Bottom Up Number factorial of {} in terms of 1,3,4 is".format(N))
print(numFactBU(N))        