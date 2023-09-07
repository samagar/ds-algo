# Problem 
# Validate BST - Left nodes should be less than right nodes
''' 
Algorithm 
Check if left is balanced
Check if right is balanced
Check if difference is > 1
All results should be either 0 or 1
'''

class BST:
    def __init__(self, value): 
        self.value = value
        self.right = None
        self.left = None

def insertNode(root,newNode):
    if root.value is None:
        root.value = newNode
    elif newNode <= root.value:
        if root.left is None:
            root.left = BST(newNode)
        else:
            insertNode(root.left, newNode)
    else:
        if root.right is None:
            root.right = BST(newNode)
        else:
            insertNode(root.right, newNode)

def levelOrderTraversal(rootNode):
    if not rootNode: return
    queue = []
    queue.append(rootNode)
    while len(queue) > 0:
        root = queue.pop(0)
        print(root.value)
   
        if root.left is not None:
            queue.append(root.left)        
        if root.right is not None:
            queue.append(root.right)

def isBalanced(root):
    return isBalancedhelper(root) > - 1

def isBalancedhelper(root):
    if root is None: return 0
    leftHeight = 1 + isBalancedhelper(root.left)
    if leftHeight == -1: return -1    
    rightHeight = 1 + isBalancedhelper(root.right)
    if rightHeight == -1: return -1

    if abs(leftHeight - rightHeight) > 1: return -1
    return max(leftHeight, rightHeight) + 1

newBST = BST(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)

insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)

print("Level Order")
print("-------------")
levelOrderTraversal(newBST)
print("Is balanced?")
print("-------------")
print(isBalanced(newBST))