class Node():
    def __init__(self, data):
        self.childLeft = None
        self.childRight = None
        self.data = data 

    def add(self, val):
        if val > self.data:
            if self.childRight != None:
                self.childRight.add(val)
                return
            self.childRight = Node(val)
        else:
            if self.childLeft != None:
                self.childLeft.add(val)
                return
            self.childLeft = Node(val)
        
    def display(self):
        if self.childLeft != None:
            self.childLeft.display()
            
        print(self.data)
        
        if self.childRight != None:
            self.childRight.display()

    def binarysearch(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.childLeft is not None:
                return self.childLeft.binarysearch(val)
            else:
                return False
        

        else:
            if self.childRight is not None:
                return self.childRight.binarysearch(val)
            else:
                return False

    def minmax(self):
        min_node = self
        while min_node.childLeft is not None:
            min_node = min_node.childLeft
        
        max_node = self
        while max_node.childRight is not None:
            max_node = max_node.childRight
        
        return (min_node.data, max_node.data)
    
    def delete(self, node):
        if self.data is None:
            print("Case 1")
            return self.data
        if self.data > node:
            print("case 2")
            if self.childLeft:
                self.childLeft = self.childLeft.delete(node)
            
        elif self.data < node:
            print("c3")
            if self.childRight:
                self.childRight = self.childRight.delete(node)
           
        else:
            print("got into else")
            
                
            if self.childLeft is None:
                print("self.childleft is none")
                return self.childRight
            elif self.childRight is None:
                print('self.childright is none')
                return self.childLeft
            elif self.childRight is None and self.childLeft is None:
                print('they are both none')
                return None
            else:
                print('else 2')
                min, max = self.childRight.minmax()
                print(min, max)
         
                self.data = min
                self.childRight = self.childRight.delete(min)
                
            


root = Node(100)
root.add(33)
root.add(50)
root.add(99)
root.add(20)
root.display()
print("")
root.delete(100)
root.display()