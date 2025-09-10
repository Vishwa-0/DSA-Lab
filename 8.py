class Node:
    def __init__(self, ts, name):
        self.ts = ts
        self.name = name
        self.left = None
        self.right = None
def insert(root, ts, name):
    if root is None:
        return Node(ts, name)
    if ts < root.ts:
        root.left = insert(root.left, ts, name)
    else:
        root.right = insert(root.right, ts, name)
    return root
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
def delete_node(root, ts):
    if root is None:
        return root
    if ts < root.ts:
        root.left = delete_node(root.left, ts)
    elif ts > root.ts:
        root.right = delete_node(root.right, ts)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value_node(root.right)
        root.ts = temp.ts
        root.name = temp.name
        root.right = delete_node(root.right, temp.ts)
    return root
def search(root, ts):
    if root is None or root.ts == ts:
        return root.name
    if ts < root.ts:
        return search(root.left, ts)
    else:
        return search(root.right, ts)
def inorder(node):
    if node:
        inorder(node.left)
        print(f"TS: {node.ts}, Name: {node.name}")
        inorder(node.right)
def preorder(node):
    if node:
        print(f"TS: {node.ts}, Name: {node.name}")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(f"TS: {node.ts}, Name: {node.name}")
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
root = None
count = 0
n = int(input("Enter number of entries: "))
for i in range(n):
    ts = int(input("Enter ts (timestamp as integer): "))
    name = input("Enter name: ")
    root = insert(root, ts, name)
    count += 1
print("\nInorder Traversal (sorted by ts):")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print(f"\nTotal number of entries: {count}")
de=int(input("Enter the timestamp of the entry to be deleted:"))
delete_node(root,de)
c=count_nodes(root)
print(f"No.of entries after deletion:{c}")
se=int(input("Enter the timestamp of the log you are searching for:"))
s=search(root,se)
print(f"The log is {se}:{s}")
print("\nPreorder Traversal(After deletion):")
preorder(root)
