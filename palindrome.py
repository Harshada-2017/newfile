s = input("Enter string: ")

stack = []

for ch in s:
    stack.append(ch)

rev = ""

while len(stack) > 0:
    rev = rev + stack.pop()

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")