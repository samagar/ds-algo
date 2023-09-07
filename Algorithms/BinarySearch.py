# Algorithms
# Searching algorithms - Binary Search

'''
- Start at 0, End at last pos and middle is center of an array.
- If value to find < middle then change end to middle - 1
- If value to find > than middle then change start to middle + 1
- Recalculate middle and repeat loop until value != middle & start <=end
- Outside loop check if value equals middle and return middle
- return -1 when value not found..

- Time Complexity O(log n) -- not all records are parsed
- Space Complexity O(1) -- Variables needs constant space
'''

import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = (start + end)// 2
    # middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        # middle = math.floor((start+end)/2)
        middle = (start + end)// 2
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
if binarySearch(custArray, 15) == -1:
    print("Value Not Found")
else:
    print('Found at index',binarySearch(custArray, 15))