word = input("Enter a string: ")

stack = []

for ch in word:
    stack.append(ch)

reverse = ""

while len(stack) > 0:
    reverse = reverse + stack.pop()

print("Reversed String:", reverse)