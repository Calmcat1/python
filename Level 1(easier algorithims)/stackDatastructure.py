class stack:
    i = 0
    arr = []

    def __init__(self):
        pass
    
    def isfull(self):
        if self.i > 80:
            return True
        
    def isempty(self):
        if self.i < -1:
            return False
      
    def addition(self, item):
        if not self.isfull():
          self.arr.append(item)
          self.i +=1
        else:
            print("the stack is full")

    def removal(self):
        try:
          self.arr.pop(self.i)
          self.i -= 1
        except IndexError:
          print("the stack is empty")

    def peek(self):
        print(self.arr)
        print(self.i)
    


stack1 = stack()
for i in range(80):
    stack1.addition('h1')
stack1.peek()
    
    
    
        