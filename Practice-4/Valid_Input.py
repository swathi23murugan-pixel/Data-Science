count = 0
while True:
    n = int(input())
    if n >= 1 and n <= 100:
        break
    print("Invalid input")
    count += 1
print("Accepted value:", n)
print("Invalid attempts:", count)