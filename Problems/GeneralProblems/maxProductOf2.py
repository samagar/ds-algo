# Problem
# Find Max Product of pair in List

def maxProduct(list):
    
    for i in range(len(list)):
        maxproduct = 0
        for j in range(i+1, len(list)):
            if (list[i] * list[j]) > maxproduct:
                maxproduct = list[i] * list[j]
                pair = str(list[i]) + "," + str(list[j])
        print(pair)
        print(maxproduct)

def maxProduct1(list):
    list.sort(reverse=True)
    print("Maxproduct",list[0] * list[1])
    print("Pair","-",list[0],",",list[1])

# Driver Code 
# Given List

my_list = [ 6, 7, 10, 11, 13 ]

# Function call
maxProduct(my_list)
maxProduct1(my_list)