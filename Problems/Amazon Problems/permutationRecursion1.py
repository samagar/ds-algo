# Problem
# Permutation without recursion

''' 
# Swap Position 1 with all positions including itself
# Fix char 1 - Swap position 2 including itself
# Fix char 2 - swap position 3 including itself - repeat till end 
'''

def toString(List):
    return ''.join(List)
 
def permute(a, l, r): # list with start and end 
    if l==r:  # if start and end position is same - return / print
        print (toString(a))
        global cnt 
        cnt += 1
    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
    return cnt


# Driver program to test the above function
string = "ABC"
global cnt
cnt = 0
n = len(string)
a = list(string)
print(permute(a, 0, n))  # n-1 because range starts at 0