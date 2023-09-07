# Minimal Binary Search Tree

# Define BST - data, left and right
# Divide BST into half and load it to get a minimum BST 

class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right
    
def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid], left, right)

# Priety Print
from collections import deque
def printTree(root):
    res = []
    q = deque([root])
    while q:
        row = []
        for _ in range(len(q)):
            node = q.popleft()
            if not node:
                row.append(" ")
                continue
            row.append(node.data)
            q.append(node.left)
            q.append(node.right)
        res.append(row)
    rows = len(res)
    base = 2**(rows)
    for r in range(rows):
        for v in res[r]:
            print(" " * (base), end = "")
            print(v, end = "")
            print(" " * (base - 1), end = "")
        print("|")
        base //= 2

# Driver code
sortedArray = [1,2,3,4,5,6,7,8,9]
bst = minimalTree(sortedArray)
printTree(bst)