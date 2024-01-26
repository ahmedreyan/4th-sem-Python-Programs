class PriorityQEntry(object):
    def __init__(self,item,priority):
        self.item=item
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.qList=list()
    def isempty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qList)
    def enqueue(self,item,priority):
        entry=PriorityQEntry(item,priority)
        if self.__len__()==0:
            self.qList.append(entry)
        else:
            for x in range(0,len(self)):
                if entry.priority >= self.qList[x].priority:
                    if x == (len(self)-1):
                        self.qList.insert(x + 1, entry)
                    else:
                        continue
                else:
                    self.qList.insert(x,entry)
                    return True
    def dequeue(self):
        assert not self.isempty(),"Cannot dequeue from an empty queue"
        return self.qList.pop(0)
    def display(self):
        for x in self.qList:
            print(str(x.item)+"-"+str(x.priority))
q=PriorityQueue()
print("Enqeue")
q.enqueue(25,3)
q.enqueue(50,2)
q.enqueue(75,1)
q.enqueue(100,6)
q.display()
print("Deqeue")
q.dequeue()
q.dequeue()
q.display
