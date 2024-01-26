class BST:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    def insert(self,data):
        if self.value:
            if data<self.value:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            elif data> self.value:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
        else:
            self.value= data
root=BST(10)
list=[20,4,30]
for i in list:
    root.insert(i)
print(list)
