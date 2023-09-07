from array import *

# Define an Array
myArray = array("i",[1,2,3,4,5])
print(myArray)

# Insert an Array
myArray.insert(5,44)
print(myArray)

# Traverse Array
for i in myArray: print(i)

# Access an Array
print(myArray[1])

# Delete an Array Element
myArray.remove(1)
print(myArray)


# String toi array
str1 = "My name is sandeep"
str1_list = list(str1)
str1_list2 = str1.split(" ")
print("$".join(str1_list2))



import random
print(random.randint(1,100))