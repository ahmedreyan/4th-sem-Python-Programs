class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
   
    def insert(self, data):
        if data < self.value:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        elif data > self.value:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)
   
    def search(self, data):
        if self.value == data:
            print("Node is Found")
            return
        elif data < self.value:
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present in the tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not present in the tree")
   
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()
   
    def delete(self, data):
        if self.value is None:
            print("Tree is Empty")
            return self
       
        if data < self.value:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("The given node is not present in the tree")
        elif data > self.value:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("The given node is not present in the tree")
        else:
            if self.left is None:
                temp = self.right
                self.right = None
                return temp
            elif self.right is None:
                temp = self.left
                self.left = None
                return temp
            else:
                min_node = self.right.find_min()
                self.value = min_node.value
                self.right = self.right.delete(min_node.value)
        return self
   
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current


root = BST(10)
data_list = [6, 12, 1, 16, 98, 3, 7]
for i in data_list:
    root.insert(i)

print("Inorder traversal before deleting the node:")
root.inorder()
print()

root.delete(6)

print("After deleting the node:")
root.inorder()
