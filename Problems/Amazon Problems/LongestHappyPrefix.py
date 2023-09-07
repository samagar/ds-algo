# Problem
# Longest happy Prefix 
# Prefix - word combinations except first char
# suffix - word combinations except last char
# When longest prefix is also a suffix then its called happy Prefix


# Problem
# Longest Happy Prefix

'''
KMP Algo - Knuth Morris & Pratt
Start j = 0 and i = 1. Compare
If equal - increament both. j is number of matches found
if no match and j > 0 then change J's position to

'''
def longest_happy_prefix(string):   
    pattern = [-1]* len(string)
    i, j = 1, 0
    while i < len(string):
        if string[i] == string[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1   # last J when you setup patter, We already increament so -1 and +1 for list correct indexing
        else:
            i += 1
    return string[0:pattern[-1] + 1]


print(longest_happy_prefix("ababaaba"))