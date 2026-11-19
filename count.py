class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print("Total nodes:", count_nodes(root))