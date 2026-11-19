class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.right.right = Node(90)

current = root

while current.right:
    current = current.right

print("Maximum value:", current.data)