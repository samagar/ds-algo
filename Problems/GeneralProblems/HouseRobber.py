# Problem
# Given N houses on street with some amount.
# Adjacent houses can not be stolen. Find maximum amount of money can be stolen.

'''

1. Start with first house. Skip one house thereafter to calculate total sum.
2. Skip with first house and skip one house thereafgter to calculate total sum
Find max of 1 & 2 as result

'''

# Divide & Conquer Approach
def houseRob(houses, currIdx):
    if currIdx >= len(houses):
        return 0
    else:
        firstHouse = houses[currIdx] + houseRob(houses, currIdx+2)
        skipFirstHouse = houseRob(houses, currIdx+1)
    return max(firstHouse,skipFirstHouse)

# Driver Code
houses = [6,7,1,30,8,2,4,55]
print("Houses \n",houses)
print("Regular Divide & Conquer \n Maximum amount that can be robbed \n",houseRob(houses, 0))


# Top Down Approach
def houseRobberTD(houses,currHouse,houseDict):
    if currHouse >= len(houses):
            return 0
    else:
        if currHouse not in houseDict:
            startFirstHouse = houses[currHouse] + houseRobberTD(houses,currHouse + 2, houseDict)
            skipFirstHouse = houseRobberTD(houses, currHouse + 1, houseDict)
            houseDict[currHouse] = max(startFirstHouse, skipFirstHouse)
        return houseDict[currHouse]

# Driver Code
houseDict = {}
print("Top down Approach \n Maximum amount that can be robbed \n",houseRobberTD(houses, 0, houseDict))


# Bottom Up approach
# Add 2 additional array elements. Store temp list and use it for calculation.
def houseRobberBU(houses):
    tempArr = [0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):  # start at end, go back, till 0
        tempArr[i] = max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]

# Driver Code
housedict = {}
print("Bottom Up Approach \n Maximum amount that can be robbed \n",houseRobberBU(houses))