# Problem
# Check if BST is Balanced
# Binary Tree is balanced if difference between right and left subtree is <= 1

''' Algorithm '''
# BSTbalanced helper function takes in root - if root is none then returns 0
# Check for left node and returns -1 if left tree is not balanced
# Check for right node and returns -1 if right tree is not balanced
# check difference between left and right tree and if if its > 1 then return -1

def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight)>1:
        return -1

    return max(leftHeight, rightHeight) + 1

def isBalanced(root):
    return isBalancedHelper(root) > -1

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N7 = Node("N7")
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6
N6.right = N7

print(isBalanced(N1))