# DataStructure
# Queue
# FIFO Array. Object to Implement Queue functionality for an Array

'''
Define Queue list, Size,Start and Stop variables 
Methods
isFull - when Top+1 = start. When start at 0 and Top+1 = Size.    
isEmpty - self.top = -1
enqueue - check if full. if top+1 = size > top=0 else Increment top. Start = 0 if -1. set value to top.

dequeue - check if empty.Get first element. if start = top > reset start & top. 
if start+1 = size > start =0 else Increament start. Set previous start to None 

peek - check first element
delete - set all items to None. Reset start and First
'''

class Queue:

    # Define Queue list, Size,Start and Stop variables 
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # isFull - when Top+1 = start. When start at 0 and Top+1 = Size.    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    # isEmpty - self.top = -1
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # enqueue - check if full. if top+1 = size > top=0. Increment top. Start = 0 of -1. set value.
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    # dequeue - check if empty.Get first element. if start = top > reset start & top. if start+1 = size > start =0. Increament start. set value
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    # peek - check first element
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    # delete - set all items to None. Reset start and First
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.delete()
print(customQueue)

