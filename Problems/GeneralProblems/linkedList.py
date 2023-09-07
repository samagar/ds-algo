# Linked List class for all problems

'''
Node class with Value, Prev and Next
Linked List class with Head and Tail
str, iter, len functions
addNode - if not head set head. Tail.next = new node. Tail = Tail.next
generateLL - head=tail-None. Add random values
'''

from random import randint

# Node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

# Linked List Class
class LinkedListClass:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:   # Existing tail = newnode, newnode = tail
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generateLL(self, n, min, max):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min,max))
        return self

customLL = LinkedListClass()
customLL.generateLL(10,0,99)
print(customLL)