
# In order. Left - root - Right

''' Algorithm'''
# Define Tree
# Check if right of this node exists - if yes then get min value from right node
# if No then go to parent - if this node is right of parent - return this parent
# if No then go till one level up parent until Top - return this

class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def minValue(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current

def inOrderSuccessor(root, n):

    # if right node is not none then get min value for this right node
    if n.right is not None:
        return minValue(n.right)
    # Else find parent - top level - ancestor of this node as in order successor
    p = n.parent
    while p is not None:
        # if node is on right of parent then stop at this parent than going up level
        if n != p.right:
            break
        n = p
        p = p.parent
    return p 

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node

from collections import deque
def printTree(root):
    res = []
    q = deque([root])
    while q:
        row = []
        for _ in range(len(q)):
            node = q.popleft()
            if not node:
                row.append("#")
                continue
            row.append(node.data)
            q.append(node.left)
            q.append(node.right)
        res.append(row)
    rows = len(res)
    base = 2**(rows)
    for r in range(rows):
        for v in res[r]:
            print("." * (base), end = "")
            print(v, end = "")
            print("." * (base - 1), end = "")
        print("|")
        base //= 2

# Driver Code
root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left #2

successor = inOrderSuccessor(root, temp)
print(successor.data)

if successor is not None:
    print("Inorder successor of %d is %d" %(temp.data, successor.data))
else:
    print("Inorder successor does not exist")

printTree(root)

