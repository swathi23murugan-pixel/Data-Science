l, r = map(int, input().split())
found = False
for i in range(1, r + 1):
    square = i * i
    if square >= l and square <= r:
        print("First perfect square:", square)
        found = True
        break
if not found:
    print("No perfect square found")