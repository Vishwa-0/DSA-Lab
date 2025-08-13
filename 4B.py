class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        nn=Node(data)
        if self.front is None:
            self.front=self.rear=nn
        self.rear.next=nn
        self.rear=nn
    def dequeue(self):
        if self.front is None:
            return None
        data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return data
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    def size(self):
        count=0
        current =self.front
        while current:
            count+=1
            current=current.next
        return count
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue elements:",)
while not q.is_empty():
    print(q.dequeue(),end=" ")
print("\nQueue is empty:",q.is_empty())
        
