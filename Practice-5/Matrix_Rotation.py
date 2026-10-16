a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(a)
b = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(a[n - 1 - j][i])
    b.append(row)
for row in b:
    print(*row)