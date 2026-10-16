a = [[0, 0, 5, 0], [0, 8, 0, 0], [3, 0, 0, 6]]
result = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] != 0:
            result.append((i, j, a[i][j]))
print(result)