# Problem
# Function to find multiple missing elements

def findMissingElements(arr, N):
 
    # Initialize diff
    diff = arr[0]
    result = []
    for i in range(N):
 
        # Check if diff and arr[i]-i
        # both are equal or not
        if(arr[i] - i != diff):
 
            # Loop for consecutive
            # missing elements
            while(diff < arr[i] - i):
                result.append(str(i+diff))
                #print(i + diff, end = " ")
                diff += 1
    return ",".join(result)


# Driver Code 
arr = [ 6, 7, 10, 11, 13 ]
N = len(arr)
print("Missing Elements -",findMissingElements(arr, N))

# Function to find one missing element in range of 100
def findOneMissingIn100(my_list, N):
    sumOfN = (N * (N+1))/2
    sumOflist = 0
    for i in my_list:
        sumOflist += i
    return int(sumOfN - sumOflist)

N = 100
my_list = []
for i in range(1,N+1):
    my_list.append(i)

my_list.remove(55)
#print("Original List \n",my_list)
print("Missing Element - ",findOneMissingIn100(my_list, N))