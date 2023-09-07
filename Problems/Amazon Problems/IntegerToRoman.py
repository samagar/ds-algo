# Problem
# Convert Number to Roman

'''
Dict of Roman values - 1,4,5,9,10,40,50,90,100,400,500,900,1000

Divide by dict keys and if > 0 then get result multiply by factor
Take remidner of number for further division

'''

def intToRoman(num):

    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 
    5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    
    for k in d.keys():
        result += (num // k) * d[k]
        num %= k
            
    return result

print(intToRoman(9))