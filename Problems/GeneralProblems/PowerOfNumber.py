# Problem
# Power of Number
'''
If Exp 0,1 then return 1, base
base*base^exp-1 recursively

'''

def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(2,3))