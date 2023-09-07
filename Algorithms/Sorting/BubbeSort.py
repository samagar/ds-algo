# Algorithm
# Bubble Sort

''' 
Inner loop > Loop through array. Start at pos 1 & swap right comparing adjacent elements. 
Outer loop > Repeat this loop for every array position.

Time complexity: O(N^2)
Space Complexity: O(N) - In place
'''

def bubbleSort(arr):
    if len(arr) == 1: return arr

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

array = [99,22,34,1,3,8,66,43,22,11,55]
print(bubbleSort(array))