a = [10, 20, 30, 40, 50]

key = int(input())

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif key < a[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found == False:
    print("Element not found")