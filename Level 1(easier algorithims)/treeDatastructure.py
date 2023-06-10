class node:
    key = 0
    left = right = None

    def __init__(self,key):
        self.key = key


class binaryTree:
    
    root = None
    
    def addNode(self,key):
        if self.root == None:
            self.root = node(key)
        else:
            if self.root.key < key:
                self.root.right = node(key)
            elif self.root.key > key:
                self.root.left = node(key)
        return f'rootnode: {self.root.key}', f'rightchildnode: {self.root.right}', f'leftchildnode: {self.root.left}'
    
    def searchNode(self,key):
        if key == self.root.key:
            return f"{key} is present in the tree"
        else:
            return f"{key} is not present in the tree"
    
    def displayNode(self):
        print(self.root.key)
  
        
        
    
    
  
binaryTree2 = binaryTree()

binaryTree2.addNode(13)
binaryTree2.addNode(26)
print(binaryTree2.addNode(9))


print(binaryTree2.searchNode(13))

binaryTree2.displayNode()






    


          
    

        
    