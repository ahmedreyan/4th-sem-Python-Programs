q=[]
def enqueue():
    if len(q)==size:
        print("Queue is Full")
    else:
        item=input("Enter the Element:")
        q.append(item)
def dequeue():
    if not q:
        print("Queue is Empty")
    else:
        item=q.pop(0)
        print("Element removed is:",item)
def display():
    if not q: #or if len(q)==0
        print("Queue is Empty")
    else:
        print(q)
size=int(input("Enter the size of Queue:"))
while(True):
    choice=int(input("1=Insert 2=Delete 3=Display 4=Quit Enter your Choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        break
