class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.value:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

user_int = input("Enter the values separated by spaces: ")
values = list(map(int, user_int.split()))
root = None
for val in values:
    root = insert(root, val)

print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
