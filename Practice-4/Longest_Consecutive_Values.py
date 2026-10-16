n = int(input())
a = list(map(int, input().split()))
current = 1
best = 1
value = a[0]
best_value = a[0]
for i in range(1, n):
    if a[i] == a[i - 1]:
        current += 1
    else:
        current = 1
    if current > best:
        best = current
        best_value = a[i]
print("Value =", best_value)
print("Length =", best)