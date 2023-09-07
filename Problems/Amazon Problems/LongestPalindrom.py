# Problem
# Longest Palindrome
# Palindrom sequence within a long string

'''
Algorithm
"babab" > char at right and char at left should match. 
Start with first 2 chars and exapnd until condition is met.
Record start and max length to get the actual string.

# Start first char as middle and expand until l = r is met -- type1 
# calculate length and start point
# Start first char and next char as middle and expand until l = r is met -- type2 
# calculate length and start point
# return length and start
# loop for all elements in string
'''
class palindrome:
    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0
        
        for i in range(len(s)):
            self.expandFromCenter(s,i,i)  # aba
            self.expandFromCenter(s,i,i+1) # abba
        return s[self.start:self.start+self.maxlen]
        

    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1

# Driver Code
s = "abccbaaaa1456bababababa12"
print(palindrome().longestPalindrome(s))