class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList:
     def __init__(self):
         self.first = None
     def insert(self, data):
         temp = Node(data)
         if(self.first):
             cur = self.first
             while(cur.next):
                 cur = cur.next
                 cur.next = temp
         else:
             self.first = temp
     def __iter__(self):
         cur = self.first
         while cur:
             yield cur.data
             cur = cur.next
# Linked List Iterators
ll = LinkedList()
ll.insert(9)
ll.insert(98)
ll.insert("welcome")
ll.insert("govt polytechnic kalaburgi")
ll.insert(456.35)
ll.insert(545)
ll.insert(5)
for x in ll:
    print(x)
