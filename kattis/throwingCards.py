class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def enqueue(self,val):
        self.__size += 1
        newNode = Node(val)
        if self.__tail == None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode
            
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

while True:
    if (n := int(input())) != 0:
        q, l, index = Queue(), [0 for _ in range(n-1)], 0
        for i in range(n):
            q.getSize()
            q.enqueue(i+1)
        while True:
            if q.getSize() == 2:
                m = q.dequeue()
                l[index] = m
                if len(l) != 0:
                    print("Discarded cards:", ", ".join(map(str,l)))
                    print("Remaining card:", q.dequeue())
                    break
                else:
                    print("Discarded cards:")
                    print("Remaining card:", q.dequeue())
                    break
            elif q.getSize() == 1:
                if len(l) != 0:
                    print("Discarded cards:", ", ".join(map(str,l)))
                    print("Remaining card: ", q.dequeue())
                    break
                else:
                    print("Discarded cards:")
                    print("Remaining card:", q.dequeue())
                    break
            else:
                m = q.dequeue()
                l[index] = m
                index += 1
                q.enqueue(q.dequeue())
    else:
        break