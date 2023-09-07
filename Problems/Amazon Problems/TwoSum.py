# Problem
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.


def twoSum(listofnum, target):
    for i in range(len(listofnum)):
        for j in range(1,len(listofnum)):
            if listofnum[i]+listofnum[j] == target:
                print(i,"-",j)

mylist = [2,7,11,15]
# twoSum(mylist,18)

def twosum1(listofnum, target):
    myDict = { value:key for key, value in enumerate(listofnum)}
    for i in range(len(listofnum)):
        trg = target - listofnum[i]

        if trg in myDict and myDict[trg] != i:
            return(i,myDict[trg])


print(twosum1(mylist,18))