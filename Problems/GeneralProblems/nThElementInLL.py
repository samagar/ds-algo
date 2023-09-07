# Problem
# Find Nth Element from last in Linked List

''' Algorithm '''
# Pointer 1 & 2 equals head
# Set pointer2 at distance N from pointer 1
# Increment both pointers by 1 and when pointer 2 reaches tail. Pointer 1 has
# End - Nth position..

from linkedList import LinkedListClass

def nThElement(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    # Set Pointer2 to Nth element from start
    for i in range(n):
        if pointer2 is None: return
        else:
            pointer2 = pointer2.next
    
    # Increment till pointer 2 is None
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedListClass()
customLL.generateLL(10,0,99)
print(customLL)
print(nThElement(customLL,3))