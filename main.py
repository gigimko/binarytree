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


root = Node(100)
root.add(33)
root.add(50)
root.add(99)
root.add(20)
print(root.binarysearch(444))
print(root.minmax())