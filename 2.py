class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def append(self,data):
        nn=Node(data)
        if self.head is None:
            self.head=nn
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=nn
    def prepend(self,data):
        if self.head is None:
            return None
        nn=Node(data)
        nn.next=self.head
        self.head=nn
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head.next
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print(None)
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Linked List:")
ll.display()
ll.prepend(0)
print("After prepending:")
ll.display()
ll.delete(2)
print("After deletion:")
ll.display()
print("search for 1:",ll.search(1))
print("search for 2:",ll.search(2))
        
