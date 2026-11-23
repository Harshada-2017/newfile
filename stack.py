class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted:", self.stack.pop())

    def display(self):
        print(self.stack)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()