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
            

root = Node(100)
root.add(33)
root.add(50)
root.add(99)
root.add(20)
root.display()