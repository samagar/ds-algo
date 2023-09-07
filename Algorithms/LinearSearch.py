# Algorithms
# Searching algorithms - Linear Search & Binary Search

'''
- Basic search all one by one
- for loop in range of length of an array and compare value and return index or else -1
'''

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([20,40,30,50,90], 90))