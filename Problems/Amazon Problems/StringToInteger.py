# Problem
# String to Integer
# Convert String into 32 bit signed integer

'''


'''

class Solution:
    def stringToI(self, str):
        result = 0
        sign = "+"
        intmax = pow(2,31) - 1
        intmin = -pow(2,31)

        for i in str:
            if i == " ": continue
            if i == "-": sign = i
            elif i.isdigit():
                result = 10 * result + int(i)
            
        if result not in range(intmin, intmax):  
            if sign == "-": return -2**31
            elif sign =="+": return 2**31-1
        else:  
            return result
 
strToIntNode = Solution()
print(strToIntNode.stringToI("  -sa123p445333222"))