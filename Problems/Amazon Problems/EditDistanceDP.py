# Problem
# Convert Strings to each other S2 <> S2 and calculate distance

'''
# Primary is Str1 which is being converted to Str2
# Compare char to char and perform either Delete, Insert or Replace Operation
# Identify min of each operation to return min distance

Operation on No Match
# Delete - Delete from STr2. Str2 +1. If Str2 End - Append Str1 remains.
# Insert - Insert str1 to Str2. Str1 +1. If Str1 End - Skip Str2 remains.
# Replace - Replace Str2 to Str2. Str +1 Str2 +1. If Str1 ends - Skip Str2 remains. 
# If Str2 ends - Append Str1 remains
'''

def convertStrings(str1, str2, idx1, idx2):
    if idx1 == len(str1): return len(str2) - idx2
    elif idx2 == len(str2): return len(str1) - idx1
    elif str1[idx1] == str2[idx2]: return convertStrings(str1, str2, idx1+1, idx2+1)
    else:
        deleteOp = 1 + convertStrings(str1,str2,idx1, idx2+1)
        insertOp = 1 + convertStrings(str1,str2,idx1+1, idx2)    
        replaceOp = 1 + convertStrings(str1,str2,idx1+1, idx2+1)
        return min(deleteOp,insertOp,replaceOp)    

# Driver Code
str1 = "sandeep"
str2 ="pradeep"

print("Edit Distance -",convertStrings(str1,str2,0, 0))