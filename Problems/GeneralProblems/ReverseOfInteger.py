# Problem
# Reverse of Integer 

'''
Convert to string and use list reversal. Convert back to int
Check overflow of 32bit signed interger - + 2**32
'''

# String function

class Solution:
    def reverse(self, x):  
        if x > 0:  a =  int(str(x)[::-1])  
        if x <=0:  a = -int(str(x*-1)[::-1])  

        # Handle 32 bit overflow   
        if a not in range(-2**31, 2**31-1):  return 0  
        else:  return a
        
print(Solution().reverse(-34843443))