class node:
    key = 0
    left = right = None

    def __init__(self,key):
        self.key = key


class binaryTree:
    
    root = None
    
    def insertNode(self,key):
        self.root  = self.insertNodeHelper(key,self.root)
        return self.root.key, self.root.left , self.root.right

    def insertNodeHelper(self, key, newnode):
        if newnode == None:
            newnode = node(key)
            return newnode
        elif newnode.key > key:
            newnode.left = self.insertNodeHelper(key,newnode.left)
        else:
            newnode.right = self.insertNodeHelper(key,newnode.right)
        return newnode

    def displayNode(self):
        pass
  
    
    def displayNodeHelper(self):
       pass
    
    def searchNode():
        pass
    
    def searchNodeHelper():
        pass
    
    def deleteNode():
        pass
     




newBinaryTree = binaryTree()

print(newBinaryTree.insertNode(5))
print(newBinaryTree.insertNode(8))
print(newBinaryTree.insertNode(3))
print(newBinaryTree.insertNode(80))








    


          
    

        
    