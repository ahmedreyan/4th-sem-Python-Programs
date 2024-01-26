class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.first = None

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.first == None:
            self.first = temp
            self.first.next = temp
        else:
            cur = self.first
            while cur.next != self.first:
                cur = cur.next
            cur.next = temp
            temp.next = self.first

    def deleteAtEnd(self):
        if self.first == None:
            print("list is empty")
        elif self.first.next == self.first:
            print("the deleted item is", self.first.data)
            self.first = None
        else:
            cur = self.first
            while cur.next != self.first:
                pr = cur
                cur = cur.next
            pr.next = self.first
            print("the deleted item is", cur.data)

    def display(self):
        if self.first == None:
            print("list is empty")
            return
        cur = self.first
        while True:
            print(cur.data)
            cur = cur.next
            if cur == self.first:
                break

    def search(self, item):
        if self.first == None:
            print("list is empty")
            return
        cur = self.first
        while cur.next != self.first:
            if cur.data == item:
                print("Item is present in the linked list")
                return
            else:
                cur = cur.next
        print("Item is not present in the linked list") 

# Circular Linked List
cll = CircularLinkedList()
while True:
    ch = int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit: "))
    if ch == 1:
        item = input("Enter the element to insert: ")
        cll.insertAtEnd(item)
        cll.display()
    elif ch == 2:
        cll.deleteAtEnd()
        cll.display()
    elif ch == 3:
        item = input("Enter the element to search: ")
        cll.search(item)
    elif ch == 4:
        cll.display()
    else:
        break
