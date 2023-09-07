# Problem
# Given items with weight and profit. Find max profit for a capacity.

'''
Divide and conquer 
Profit of items skipping first item till capacity
Profit of items with first item till capacity

'''

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsack(items, capacity, currIndex):
    if capacity <=0 or currIndex >= len(items) or currIndex < 0: return 0
    elif items[currIndex].weight < capacity:
        profit1 = items[currIndex].profit + zoKnapsack(items,capacity-items[currIndex].weight, currIndex+1)
        profit2 = zoKnapsack(items,capacity, currIndex+1)
        return max(profit1,profit2)
    else: return 0
    
mango = Item(31,3)
apple = Item(26,1)
orange = Item(17,2)
banana = Item(72,5)

items = [mango, apple, orange, banana]

# print(zoKnapsack(items,7,0))



# Regular approach

items = [["Mango",31,3],["apple",26,1],["orange",17,2],["banana",72,5]]

def zoKnapsack1(items, capacity):
    item_upload = []
    profit  = 0

    for key in items:
        key.append(round(key[1]/key[2],2))

    items.sort(key=lambda x : x[3], reverse=True)
    print(items)

    for fruits in items:
        weight = fruits[2]

        if capacity >= weight:
            item_upload.append(fruits[0])
            profit += fruits[1]                        
            capacity -= weight
        
    return profit

print(zoKnapsack1(items,7))