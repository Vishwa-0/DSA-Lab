MAX_SIZE=5
stack=[]
top=-1
def push(book_tittle):
    global top
    if top>=MAX_SIZE-1:
        print("Stack overflow cannot push new tittles")
    else:
        top+=1
        stack.append(book_tittle)
        print(f"Book '{book_tittle}' is pushd into the stack")
def pop():
    global top
    if top==-1:
        print("Stack underflow cannot pop any books")
    else:
        popped_book=stack.pop()
        print(f"The popped book is '{popped_book}'")
        top-=1
def peek():
    if top==-1:
        print("Stack is empty")
    else:
        print(f"Top book in the stack is:'{stack[top]}'")
def display():
    if top==-1:
        print("Stack is empty")
    else:
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("Mistborn")
push("Stormlight Archive")
push("The Black Company")
push("The poppy War")
push("Keeping the dead")
push("Broken Earth")
display()
pop()
pop()
peek()
display()
