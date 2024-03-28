class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.count = -1
    
    def add(self,val):
        if self.root == None:
            self.root = self.createNewNode(val)
            self.count += 1
            print(self.count)
        else: 
            parent = None
            current = self.root
            while current != None:
                if current.element >= val:
                    parent = current
                    current = current.left
                    self.count += 1
                else:
                    parent = current
                    current = current.right
                    self.count += 1
            
            self.size += 1
            if val <= parent.element:
                parent.left = self.createNewNode(val)
            else:
                parent.right = self.createNewNode(val)
            print(self.count)
    
    def kidKiller(self, val):
        pass
    
    def kidTracker(self, val):
        current = self.root
        while current != None:
            if current.element > val:
                current = current.left
            elif current.element < val:
                current = current.right
            else:
                return True
        return False
        
    def createNewNode(self, e):
        return TreeNode(e)

    def getSize(self):
        return self.size
    
    def preOrder(self):
        self._preOrderHelper(self.root)
    
    def _preOrderHelper(self, v):
        if v != None:
            print(v.element, end = " ")
            self._preOrderHelper(v.left)
            self._preOrderHelper(v.right)
    
    def postOrder(self):
        self._postOrderHelper(self.root)
        
    def _postOrderHelper(self, v):
        if v != None:
            self._postOrderHelper(v.left)
            self._postOrderHelper(v.right)
            print(v.element, end = " ")
    
    def inOrder(self):
        self._inOrderHelper(self.root)
    
    def _inOrderHelper(self,v):
        if v != None:
            self._inOrderHelper(v.left)
            print(v.element, end = " ")
            self._inOrderHelper(v.right)
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


b = BST()
for i in range(int(input())):
    b.add(input())