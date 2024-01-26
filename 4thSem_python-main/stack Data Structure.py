#Implement Stack Data Structure.
s = []
def push():
    if len(s) == size:        
        print("Stack is Full")
    else:
      item = input("Enter the element:")
      s.append(item)
def pop():
    if(len(s) == 0):
        print("Stack is Empty")
    else:
        item = s[-1]
        del(s[-1])
        print("The deleted element is:",item)
def display():
    size = len(s)
    if(size== 0):
        print("Stack is Empty")
    else:
        for i in reversed(s):
            print(i)

#Execution starts here
size=int(input("Enter the size of Stack:"))

while(True):
    choice = int(input("1-Push 2-POP 3-DISPLAY 4-EXIT Enter your choice:"))
    if(choice == 1):
        push()
    elif(choice == 2):
         pop()
    elif(choice == 3):
         display()
    else:
        break
