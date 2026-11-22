size = 5
queue = [0] * size

front = -1
rear = -1

def enqueue(data):
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is full")
    else:
        if front == -1:
            front = 0

        rear = (rear + 1) % size
        queue[rear] = data


def dequeue():
    global front, rear

    if front == -1:
        print("Queue is empty")
    else:
        print("Deleted:", queue[front])

        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size


def display():
    if front == -1:
        print("Queue is empty")
    else:
        i = front
        while True:
            print(queue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size


enqueue(10)
enqueue(20)
enqueue(30)
display()
print()
dequeue()
display()