class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def findval(self, ikpval):
        if ikpval < self.data:
            if self.left is None:
                return str(ikpval) + "not found"
            return self.left.findval(ikpval)
        elif ikpval > self.data:
            if self.right is None:
                return str(ikpval) + "not found"
            return self.right.findval(ikpval)
        else:
            print(str(self.data) + 'is found')

root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()
print(root.findval(7))
print(root.findval(35))