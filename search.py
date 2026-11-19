class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        if self.root is None:
            self.root = new
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    return
                current = current.right

    def search(self, data):
        current = self.root

        while current:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False


tree = BST()

for i in [50, 30, 70, 20, 40]:
    tree.insert(i)

print(tree.search(40))
print(tree.search(90))