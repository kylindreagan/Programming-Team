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

class Node:
    def __init__(self, data):
        self.element= data 
        self.next = None

n, T = map(int, input().split())
tasks = [int(x) for x in input().split()]
q = Queue()

for i in tasks:
    q.enqueue(i)

runningT = 0
steps = 0
for j in range(n):
    if runningT + q.peek() > T:
        break
    else:
        runningT += q.dequeue()
        steps += 1

print(steps)