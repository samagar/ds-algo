# Problem
# Print Permutation of given list
# Number of ways a given list of items can be arranged
# e.g. How many ways 0-9 digits can be arranged in 3 digit keypad > p(9,3)
# P(n,r) = n! / (n-r)! 

'''
Take first item in list. Append to result.
Recursively call for list remaining items - concat first item with returns. 
End conditions - 0 return None, 1 return list
'''

def permutation(lst):
    if len(lst) == 0: return []
    if len(lst) == 1: return[lst]
    l = [] 

    for i in range(len(lst)):
        m = lst[i] 
        remLst = lst[:i] + lst[i+1:] 
        for p in permutation(remLst):
            l.append([m] + p)
    return l

# Driver program to test above function
data = list('12332323')
print("Number of Permutations for List -", data, ">", len(permutation(data)))