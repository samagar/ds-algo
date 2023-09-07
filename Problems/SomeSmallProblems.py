# Some Small Problems

# Flat an Array
def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 

myarr = [[1,2,3],[3,4],[5,6]]
print(flatten(myarr))


# Capitalize First Letter
def capitalizeFirst(string):
    listofstring = string.split(" ")
    listofstring = [i[0].upper() + i[1:] for i in listofstring]
    return " ".join(listofstring)

print(capitalizeFirst("my name is sandeep"))


# Sum of Even Numbers in a Nested Object
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum


# Stringify number 
def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj


# Collect Strings
def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr


# Copy list into another except for first and last elements.

def middleList(my_list):
    result = [my_list[i] for i in range(1,len(my_list)-1)]
    print(result)

my_list = [1,2,3,4,5,6]
middleList(my_list)


# Sum of Diagonal Elements

def sumOfDiagonalElements(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i][i]
    
    print(sum)

my_list = [[1,2,3],[4,5,6],[7,8,9]]
sumOfDiagonalElements(my_list)

# Palindrom
def isPalindrome(strng):
    return True if strng[::-1] == strng else False

print(isPalindrome("Neil"))
