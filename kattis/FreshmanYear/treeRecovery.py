class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.key = {}
    
    def add(self,val):
        if self.root == None:
            self.root = self.createNewNode(val)
        else: 
            parent = None
            current = self.root
            while current != None:
                if current.element >= val:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
            
            self.size += 1
            if val <= parent.element:
                parent.left = self.createNewNode(val)
            else:
                parent.right = self.createNewNode(val)
    
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
            print(self.key[v.element], end = "")
    
    def inOrder(self):
        self._inOrderHelper(self.root)
    
    def _inOrderHelper(self,v):
        if v != None:
            self._inOrderHelper(v.left)
            print(v.element, end = " ")
            self._inOrderHelper(v.right)
    
    def changeKey(self, d):
        self.key = d

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None

def main():
    try:
        while 1:
            preord, inord = map(str, input().split())
            d1,d2= {},{}
            n, head, x = len(preord), preord[0], 0
            hindex = inord.find(head)
            b = BST()
            for j in inord:
                d1[x] = j
                d2[j] = x
                x+=1
            b.changeKey(d1)
            for i in preord:
                b.add(d2[i])
            b.postOrder()
            print()
    except :
        quit()
main()