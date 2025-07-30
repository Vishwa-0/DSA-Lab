class Node:
    def __init__(self,data):
        self.data=data
        self.top=None
class Stack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top is None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_data=self.top.data
            self.top=self.top.next
    def peek(self):
        if self.top is None:
            return None
        else:
            print(f"The top value is:{stack.top.data}")
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.pop()
stack.pop()
stack.peek()
