# Problem
# Count min number of operations required to convert one string to another

'''

To convert str1 to str2; you would either need to delete, insert or replace 
chars from one string to another

calculate number of delete, insert and replace operations required 
Return min to provide to tell which operation would take minimum

Compare 1 - 1. If match move to next. 
Delete - If no match then increase index of str2 then Attach remaining from str1 
if str2 is at end.
Insert - If no match then insert str1 char and increase index of str1. 
If Str1 is at end then skip str2 remaining chars.
Replace - If no match then replace chars. Increate index of both. If str1 ends
then skip remaining and if str2 ends then attach remaining. 

'''

def convStrOps(str1, str2, idx1, idx2):
    if idx1 == len(str1):
        return len(str2)-idx2
    elif idx2 == len(str2): 
        return len(str1)-idx1
    elif str1[idx1] == str2[idx2]: 
        return convStrOps(str1, str2, idx1+1, idx2+1)
    else:
        # every operation is one ops so "1 +" 
        # for delete operation char from 2nd string is deleted hence "idx2+1" -- increment second string
        deleteOp = 1 + convStrOps(str1,str2,idx1, idx2+1)
        # for insert operation char from 1st string is inserted hence "idx1+1" -- increament first string    
        insertOp = 1 + convStrOps(str1,str2,idx1+1, idx2)           
        # for replace operation; increament char from both strings
        replaceOp = 1 + convStrOps(str1,str2,idx1+1, idx2+1)
        return min(deleteOp,insertOp,replaceOp)    
        
# Driver Code
str1 = "sandeep"
str2 = "pradeep"
#print(str1)
#print(str2)
print("Number of disposition for two strings above \n",convStrOps(str1,str2,0,0))
