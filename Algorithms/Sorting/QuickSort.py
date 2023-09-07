# Algorithm
# Quick Sort

''' 
Divide & conquer alorithm
Consider arr[0] or 1st position as pivot (it can be last as well)
Divide array in 3 parts - Array1 (elements < 1st element) + 1st + Array2 (elements > 1st element)
Recursion on Array1 & Array2 - This will ensure full sorting of each array
Return Sorrted Array1 + 1st element + Sorted Array2

Time Complexity:O(NlogN)
Space Complexity:O(N) - In place

'''

# Quick Sort Using Recursion

def quicksort(arr):
    if arr: 
        return (quicksort([i for i in arr[1:] if i < arr[0]] )
                + [arr[0]] 
                + quicksort([i for i in arr[1:] if i >= arr[0]]))
    else: 
        return arr

array = [35,2,3,54,3,4]
print("Unsorted Array \n",array)
print("Sorted Array \n",quicksort(array))

# Quick Sort Without Recursion
'''
- Make a set of low and high position of an array.
- Loop till Stack exists
- Call partition function with low and high position and array
- Note high position value as pivote and low pos - 1 as sort position
- Loop through array. If any loop position value is < pivot then 
  Increment sort position and swap loop position with sort position. 
- Outside loop - Increment sort positin and swap to handle edge conditions.
- Return sort position - This indicates that sorting is done till this point.
- Change the stack to remove sorted position - reduce the stack till its empty
'''
def QuickSort(arr):
    if len(arr) <= 1: return arr
    stack = [(arr, len(arr)-1)]

    while stack:
        low, high = stack.pop()
        pivot_index = partition(arr, low, high)

        if pivot_index - 1 > low:
            stack.append(low, pivot_index - 1)
        if pivot_index + 1 < high:
            stack.append(pivot_index + 1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high, arr[i+1]]
    return i+1