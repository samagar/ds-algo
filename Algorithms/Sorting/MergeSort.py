# Algorithm
# Merge Sort

''' 
Divide array into 2 parts at mid - left & right. Call recursion on left & right arrays.
Merge function that takes left & right arrays as input.
While loop till atlest 1 item in both arrays.
    write lesser element in new output array
Write leftovers from both array to output array

Time Complexity:
O(NlogN)  => half array traveral parallel

Space Complexity:
O(N)

''' 

def mergeSort(arr):
    if len(arr) == 1: return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])     # n/2 time
    right = mergeSort(arr[mid:])    # n/2 time >> nlogn

    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output

array = [5,50,23,22,1,2,7,8]
print("unsorted", array)
print("sorted",mergeSort(array))