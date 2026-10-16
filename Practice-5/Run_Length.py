values = [4, 4, 4, 2, 2, 7, 7, 4, 4, 9]
compressed = []
count = 1
for i in range(1, len(values)):
    if values[i] == values[i - 1]:
        count += 1
    else:
        compressed.append((values[i - 1], count))
        count = 1
if values:
    compressed.append((values[-1], count))
print("Compressed list:", compressed)