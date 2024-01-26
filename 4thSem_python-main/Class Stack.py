class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        return(self.items)

s=stack()
s.display()
s.isempty()
s.push(11)
s.push(12)
s.push(13)
s.display()
print("Popped item is:",s.pop())
print("Size is:",s.size())
print("Top item is :",s.peek())
