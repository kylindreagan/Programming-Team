class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def push(self, val):
        newNode = Node(val)
        if self.__head == None:
            self.__head = newNode
            self.__size += 1
        else:
            newNode.next = self.__head
            self.__head = newNode
            self.__size += 1
        
    
    def peek(self):
        if self.__head == None:
            raise IndexError
        return self.__head.element
    
    def pop(self):
        if self.__head == None:
            raise IndexError 
        val = self.peek()
        self.__head = self.__head.next
        self.__size -= 1
        return val
    
    def isEmpty(self):
        return self.__head == None
    
    def getSize(self):
        return self.__size

class Node:
    def __init__(self, data):
        self.element= data 
        self.next = None

n = int(input())

originalPile = Stack()
originalPileList = input().split()

for i in originalPileList:
    originalPile.push(i)
    
opSet = set(originalPileList)
auxiliaryPile = Stack()
steps = 0

if len(opSet) == 1:
    print(2*n)
elif len(opSet) > n:
    print("impossible")
else:
    while True:
        if originalPile.isEmpty() and auxiliaryPile.isEmpty():
            break
        
        elif originalPile.isEmpty():
            steps = "impossible"
            break
        
        elif auxiliaryPile.isEmpty():
            auxiliaryPile.push(originalPile.pop())
            steps += 1
        
        if originalPile.peek() == auxiliaryPile.peek():
            originalPile.pop()
            auxiliaryPile.pop()
            steps += 1
        
        else:
            auxiliaryPile.push(originalPile.pop())
            steps += 1
        
    print(steps)