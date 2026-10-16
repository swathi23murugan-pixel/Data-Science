a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = []
for i in range(len(a)):
    if i % 2 == 0:
        result.extend(a[i])
    else:
        result.extend(a[i][::-1])
print("Zigzag list:", result)