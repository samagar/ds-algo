# Problem
# Find Depth of binary tree
''' Algorithm '''
# Check if root exists - return 0 
# Check if left and right nodes both dont exists  - return 1
# Find depath of right and left child nodes - add + 1
# return greater from left or right child node


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree == None:
        return 0
    if tree.left == None  and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight

mainTree = BinaryTree(1)
mainTree.left = BinaryTree(2)
mainTree.right = BinaryTree(3)
mainTree.left.left = BinaryTree(4)
mainTree.left.right = BinaryTree(5)
mainTree.right.left = BinaryTree(6)
mainTree.right.right = BinaryTree(7)

print(depth(mainTree))