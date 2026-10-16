a = [10, 20, 30, 40]
b = [1, 2, 3, 4]
c = []
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
print("Interleaved list:", c)