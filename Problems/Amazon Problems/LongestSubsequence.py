# Problem
# Longest repeated subsequence

'''
Subsequence is a sub string that can be achieved from a string by deleting one or more chars
Repeated subsequence is subsequence thats repeated atleast 2 times

Take 2 indexes pointing to end of string
When chars at both index match & indexes are different - call recursion + 1
If either m or n reaches start of string - return 0

'''
def LRSLength(X, m, n):
    if m == 0 or n == 0: return 0

    # if value at index m & n matches and m is not equal n, Decrement both
    if X[m - 1] == X[n - 1] and m != n:       
        return LRSLength(X, m-1, n-1) + 1

    # if chars dont match then get max of either char -1
    return max(LRSLength(X, m, n-1), LRSLength(X, m-1, n))
 
print(LRSLength("ATAKTKGGB",9,9))