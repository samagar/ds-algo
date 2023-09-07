# Problem
# Median Sorted Arrays

'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

Regular
merge Lists. Get Median Index. if even then median index + 1. Else median index + median index + 1 /2
'''

class Solution:
    def findMedianSortedArrays(self, num1, num2):
        num = num1 + num2  # 1
        num.sort()   # nlog(m+n)
        medianIndex = len(num)//2 - 1  # list starts at 0
    
        if len(num)%2 != 0:
            median = num[medianIndex + 1]
        else: 
            median = (num[medianIndex] + num[medianIndex + 1])/2

        print("median",median)
            
    
num1 = [1,2]
num2 = [3,5]

findMedian = Solution()
findMedian.findMedianSortedArrays(num1,num2)


