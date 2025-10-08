class DoublyCircularLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__reverse = False
        self.__size = 0
    
    def pushHead(self, val):
        newNode = Node(val)
        if self.__head == None:
            self.__head = self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.prev = newNode
            self.__head.next = newNode
            newNode.next = self.__head
            newNode.prev = self.__tail
            self.__head = newNode
            self.__size += 1
    
    def pushTail(self,val):
        newNode = Node(val)
        if self.__tail == None:
            self.__head = self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.next = newNode
            self.__head.prev = newNode
            newNode.prev = self.__tail
            newNode.next = self.__head
            self.__tail = newNode
            self.__size += 1
    
    def returnList(self):
        if not self.__reverse:
            result = "["
    
            current = self.__head
            for i in range(self.__size):
                result += str(current.element)
                current = current.next
                if i != self.__size - 1:
                    result += "," # Separate two elements with a comma
                else:
                    result += "]" # Insert the closing ] in the string
    
            return result
        else:
            result = "["
    
            current = self.__tail
            for i in range(self.__size):
                result += str(current.element)
                current = current.prev
                if i != self.__size - 1:
                    result += "," # Separate two elements with a comma
                else:
                    result += "]" # Insert the closing ] in the string
    
            return result
    
    # Return true if this list contains the element o 
    def contains(self, e):
        if e in self:
            return True
        
    def removeHead(self):
        if self.__reverse:
            if self.__size == 0:
                return None # Nothing to delete
            else:
                temp = self.__tail # Keep the first node temporarily
                self.__tail = self.__tail.prev # Move head to point the next node
                self.__tail.next = self.__head
                self.__size -= 1 # Reduce size by 1
                if self.__tail == None: 
                    self.__head = None # List becomes empty 
                return temp.element
        else:
            if self.__size == 0:
                return None # Nothing to delete
            else:
                temp = self.__head # Keep the first node temporarily
                self.__head = self.__head.next # Move head to point the next node
                self.__head.prev = self.__tail
                self.__size -= 1 # Reduce size by 1
                if self.__head == None: 
                    self.__tail = None # List becomes empty 
                return temp.element
    
    def reverse(self):
        if self.__reverse:
            self.__reverse = False
        else:
            self.__reverse = True

class Node:
    def __init__(self, data):
        self.element= data 
        self.next = None
        self.prev = None

for i in range(int(input())):
    BAPC = input()
    deletes = BAPC.count("D")
    n = int(input())
    inputListStr = input().strip('[').strip(']').strip()
    if deletes > n:
        print("error")
    elif deletes == n:
        print("[]")
    elif deletes == 0:
        reverses = BAPC.count("R")
        if reverses % 2 == 0:
            print("[" + inputListStr + "]")
        else:
            inputList = [int(x) for x in inputListStr[::-1].split(",")]
            print("[", end="")
            for h in range(len(inputList)):
                if h == len(inputList) - 1:
                    print(inputList[h], end="")
                    print("]")
                else:
                    print(inputList[h], end=",")
    else:
        inputList = [int(x) for x in inputListStr.split(",")]
        linkInputList = DoublyCircularLinkedList()
        for i in inputList:
            linkInputList.pushTail(i)
        for j in BAPC:
            if j == "R":
                linkInputList.reverse()
            else:
                linkInputList.removeHead()
                
        print(linkInputList.returnList())