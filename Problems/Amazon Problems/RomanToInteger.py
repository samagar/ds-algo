# Problem
# Roman to Integer

'''
Start at 1 to length + 1 for integer 
if value > temp - add+value else add-value. Save Temp = value
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        add=0
        temp=0
        for i in range (1,len(s)+1):
            if dict[s[-i]]>=temp:
                add+=dict[s[-i]]
            else:
                add-=dict[s[-i]]
            temp=dict[s[-i]]
        return add

myObj = Solution()
print(myObj.romanToInt("MD"))