# Problem 
# Validate BST - Left nodes should be less than right nodes
''' Algorithm '''
# Check basic condition of not Node - return True
# Check if value of node is less than min or max node -- start with infinity
# Check for right node where in right node should be > value and < max inf
# Check for left node where in left node should be less than value & < min -inf

class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None

def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node:return True
    val = node.val
    if val <= minValue or val >= maxValue:return False
    if not helper(node.right, val, maxValue):return False
    if not helper(node.left, minValue, val):return False
    return True

def isValidBST(root):
    return helper(root)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

print(isValidBST(root1))

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(isValidBST(root2))