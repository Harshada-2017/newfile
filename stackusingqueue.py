class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Deleted:", self.top.data)
            self.top = self.top.next

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
print()
s.pop()
s.display()