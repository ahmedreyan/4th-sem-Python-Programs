class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.first=None
    def insertfirst(self,data):
        temp=node(data)
        temp.next=self.first
        self.first=temp
    def removefirst(self):
        if(self.first==None):
            print("List is Empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("The deleted item is:",cur.data)
    def display(self):
        if(self.first==None):
            print("List is Empty")
            return
        cur=self.first
        while(cur):
            print(cur.data)
            cur=cur.next
    def search(self,item):
        if(self.first==None):
            print("List is Empty")
            return
        cur=self.first
        while cur!=None:
                if cur.data==item:
                    print("Item is present in Linked List")
                    return
                else:
                    cur=cur.next
        print("Item is not present in Linked List")
            #Singly Linked List
sll = singlylinkedlist()
while(True):
    ch = int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit :"))
    if(ch == 1):
        item = input("Enter the element to insert:")
        sll.insertfirst(item)
        sll.display()
    elif(ch == 2):
        sll.removefirst()
        sll.display()
    elif(ch==3):
        item=input("Enter the element to search:")
        sll.search(item)
    elif(ch==4):
        sll.display()
    else:
        break
            #output
