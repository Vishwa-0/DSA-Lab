class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def build_tree():
    value = input("Enter node value: ")
    node = TreeNode(int(value))
    num_children = int(input(f"Enter number of children for node {value}: "))
    for i in range(num_children):
        print(f"Entering child {i+1} of node {value}:")
        child = build_tree()
        node.add_child(child)
    return node

def preorder_traversal(node, result=None):
    if result is None:
        result = []
    result.append(node.value)
    for child in node.children:
        preorder_traversal(child, result)
    return result

def inorder_traversal(node, result=None):
    if result is None:
        result = []
    if node.children:
        inorder_traversal(node.children[0], result)
    result.append(node.value)
    for child in node.children[1:]:
        inorder_traversal(child, result)
    return result

def postorder_traversal(node, result=None):
    if result is None:
        result = []
    for child in node.children:
        postorder_traversal(child, result)
    result.append(node.value)
    return result

if __name__ == "__main__":
    print("Build your tree:")
    root = build_tree()
    print("\nTree Structure:")
    print(root)

    print("Inorder:", inorder_traversal(root))
    print("Preorder:", preorder_traversal(root))
    print("Postorder:", postorder_traversal(root))

