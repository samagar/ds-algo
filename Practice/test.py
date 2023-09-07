# permutation

from re import A


def permutation(listA):
    if len(listA) == 0: return []
    if len(listA) == 1: return [listA]
    combi = []
    
    for i in range(len(listA)):
        var1 = listA[i]
        remain = listA[:i] + listA[i+1:]
        for p in permutation(remain):
            combi.append([var1] + p)

    return combi


# Driver
listA = list('123456')
print(len(permutation(listA)))
