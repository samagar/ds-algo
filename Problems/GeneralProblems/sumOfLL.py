# Problem
# Sum 2 linked lists storing each digit of a number as a node
# return sum linked list storing each digit as node in reverse order

from linkedList import LinkedListClass

def sumOfLL(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedListClass()

    while n1 or n2:
        result = carry 
        if n1:
            result += n1.value
            n1 = n1.next
        
        if n2:
            result += n2.value
            n2 = n2.next
        
        ll.add(int(result % 10))
        carry = result / 10
    return ll
    
customLL1 = LinkedListClass()
customLL1.generateLL(3,1,9)
print(customLL1)
customLL2 = LinkedListClass()
customLL2.generateLL(3,1,9)
print(customLL2)
print("---sum---")
print(sumOfLL(customLL1,customLL2))