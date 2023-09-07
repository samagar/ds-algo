''' Binary Search tree '''
# Tree with Nodex and upto 2 children.
# Left child will have lesser value than right child

# Define BST
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
# Insert Node
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

# Treee Traversal
def preOrderTraversal(rootNode):
    if not rootNode:return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)          

# Search node
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

# Check root. Print root, queue left child. queue right child.
# BFS Method - Queue
def levelOrderTraversal1(rootNode):
    if not rootNode:return
    else:
        queue = []
        queue.append(rootNode)
        while len(queue) > 0:
            root = queue.pop(0)
            print(root.data)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)

# Get Min Value
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

# Start with Root node and Traverse till Node is found
# If node has no children - delete leaf node
# If node has one child - Replace node with child. Delete child leaf node
# If node has 2 children - Replace Node with min value child in right sub tree. 
# ...and Delete that min value node.

def deleteNode(rootNode, nodeValue):
    if rootNode is None:return rootNode    

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# Delete whole Tree
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"


from collections import deque
def print_tree(root):
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
            q.append(node.leftChild)
            q.append(node.rightChild)
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

        
def myPrint(rootNode):
    if not rootNode:return
    print(rootNode.data)
    print("Left")
    preOrderTraversal(rootNode.leftChild)
    print("right")
    preOrderTraversal(rootNode.rightChild)

  
   
newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
preOrderTraversal(newBST)
deleteNode(newBST,70)
preOrderTraversal(newBST)
myPrint(newBST)
print_tree(newBST)
print(levelOrderTraversal1(newBST))
print(deleteBST(newBST))
#levelOrderTraversal(newBST)
