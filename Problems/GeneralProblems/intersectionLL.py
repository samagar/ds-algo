# Problem
# Find intersection of 2 linked lists.
# Two linked lists can meet at a Node and continues through common nodes
# i.e. Tail nodes of both LL is same.

'''
Generate Linked list using Linked List custom class.
Add common node using helper function - to generate scenario.
# Find long and Short LL. 
# Skip non intersecting nodes using diff in long node. 
# compare long and short nodes to find match and return long node

'''

# Linked List custom class import  - optional
from linkedList import LinkedListClass, Node

# Main Intersection finder function
def intersection(llA, llB):
    # Ensure LLs are intersecting
    if llA.tail != llB.tail: return False

    # Find long and Short LL. 
    # Skip non intersecting nodes using diff in long node. 
    # compare long and short nodes to find match and return long node

    short = llB if len(llA) > len(llB) else llA
    long = llB if len(llB) > len(llA) else llA

    diff = len(long) - len(short)
    
    longNode = long.head
    shortNode = short.head

    for i in range(diff):
        longNode = longNode.next

    while shortNode is not longNode:
        shortNode = shortNode.next
        longNode = longNode.next

    return longNode


# Helper Function - Add common Node
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

# Generate LL and Intersecting nodes
customLL1 = LinkedListClass()
customLL1.generateLL(7,1,25)
print(customLL1)
customLL2 = LinkedListClass()
customLL2.generateLL(9,26,60)
print(customLL2)
addSameNode(customLL1,customLL2, 30)
addSameNode(customLL1,customLL2, 55)
addSameNode(customLL1,customLL2, 78)

print(customLL1)
print(customLL2)

print(intersection(customLL1,customLL2))