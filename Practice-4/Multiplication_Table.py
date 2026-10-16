n = int(input())
count = 0
for i in range(1, 21):
    result = n * i
    if result > 100:
        break
    if result % 3 == 0:
        count += 1
        continue
    print(n, "x", i, "=", result)
print("Skipped results:", count)