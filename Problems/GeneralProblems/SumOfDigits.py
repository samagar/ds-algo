# Problem
# Sum Of Digits

'''
(Number % 10) > Reminder + Recursion (Number / 10)
Divide number by 10 and add reminder one a time until n = 0
'''

def sumofDigits(n):
    assert n>=0 and int(n) == n , 'The number has to be a postive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(1233))