n = int(input("Enter a number: "))
seen = set()

while n != 1 and n not in seen and n > 0:
    seen.add(n)
    total = 0

    for digit in str(n):
        total += int(digit) ** 2

    n = total

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")