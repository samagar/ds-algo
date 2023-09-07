# Problem
# Remove duplicates from linked list

from linkedList import LinkedListClass

def removeDuplicates(ll):
    if ll.head is None: return
    else:
        tempNode = ll.head
        visited = set([tempNode.value])
        while tempNode.next:
            if tempNode.next.value in visited:
                tempNode.next = tempNode.next.next
            else:
                visited.add(tempNode.next.value)
                tempNode = tempNode.next
        return ll

def removeDuplicates1(ll):
    if ll.head is None: return
    tempNode = ll.head
    while tempNode:
        runner = tempNode
        while runner.next:
            if runner.next.value == tempNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        tempNode = tempNode.next
    return ll.head

customLL = LinkedListClass()
customLL.generateLL(10,0,15)
print(customLL)
removeDuplicates(customLL)
print(customLL)
removeDuplicates1(customLL)
print(customLL)