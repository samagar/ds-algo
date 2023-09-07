# Problem
# Arrange Linked list around a partition key. < befoe and > after.

from linkedList import LinkedListClass

def partition(ll, x):
    currNode = ll.head
    ll.tail = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < x:
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode 
            ll.tail = currNode
        currNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None
    
customLL = LinkedListClass()
customLL.generateLL(10,0,40)
print(customLL)
partition(customLL, 30)
print(customLL)