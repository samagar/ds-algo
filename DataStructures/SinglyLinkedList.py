# Data Structure
# Linked List - Singly Linked List
# Singly Linked List has vlaue and link to next item

'''

# Singly Linked List
# Define Value and Next as Node.Define Head and Tail.
# To Insert - at begining, In middle, At End
# Insert middle - Stop before location. Temp = Location (Stop.next)
# nextNode = location.next. location.next = Newnode. newNode.next = nextNode 

'''

# Define Node Class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
# Define Singly linked list class
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method to print 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    # Method to insert a Node in link list 
    def InsertNode(self, value, location):
        newnode = Node(value)  # Create Node for value 
        if self.head is None:   # If first then populate head & tail
            self.head = newnode
            self.tail = newnode
			# if Insert at begining - set existing head as next of new node 
        else:
            if location == 0:     
                newnode.next = self.head
                self.head = newnode
			# Insert at End - set Next of Existing tail node as new node                
            elif location == -1:  
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                # Insert middle - Find an element before location and set its next
                # Start with head node and index 0. Stop before location -1. Skip next. 
                tempnode = self.head 
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
                
                if tempnode == self.tail:  # If its last node insert by location then update tail value
                     self.tail=newnode
            
            
    # Traverse Singly Linked List
    def TraverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    # Search for a node in Singly Linked List
    def SearchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
        
    #  Delete a node from Singly Linked List
    def DeleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    # Delete entire SLL
    def DeleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None



# Core Driver Program
NodeObj = SLinkedList()
NodeObj.InsertNode(1,0)
NodeObj.InsertNode(2,0)
NodeObj.InsertNode(3,0)
NodeObj.InsertNode(4,0)
NodeObj.InsertNode(5,-1)
NodeObj.InsertNode(8,-1)
NodeObj.InsertNode(11,3)
NodeObj.InsertNode(17,3)
NodeObj.InsertNode(26,8)
print([node.value for node in NodeObj]) 
print(NodeObj.SearchSLL(17))
print(NodeObj.SearchSLL(99))
NodeObj.DeleteNode(5)
print([node.value for node in NodeObj])