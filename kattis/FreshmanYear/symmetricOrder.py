class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def enqueue(self,val):
        newNode = Node(val)
        if self.__tail == None:
            self.__head = self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.next = newNode
            self.__tail = newNode
            self.__size += 1
    def peek(self):
        if self.__head == None:
            raise IndexError
        return self.__head.element
    
    def dequeue(self):
        if self.__head == None:
            raise IndexError 
        val = self.peek()
        self.__head = self.__head.next
        self.__size -= 1
        return val
    
    def empty(self):
        return self.__head == None
    
    def getSize(self):
        return self.__size

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
    
    def empty(self):
        return self.__head == None
    
    def getSize(self):
        return self.__size

class Node:
    def __init__(self, data):
        self.element= data 
        self.next = None

tracker = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        q, s = Queue(), Stack() 
        for i in range(n):
            if i % 2 == 0:
                q.enqueue(input())
            else:
                s.push(input())
        print("SET", tracker)
        for j in range(q.getSize()):
            print(q.dequeue())
        for h in range(s.getSize()):
            print(s.pop())
        tracker += 1