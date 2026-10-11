n = int(input("Enter a number: "))

print("Prime:", end=" ")
if n > 1:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    print("Yes" if prime else "No")
else:
    print("No")

digit_sum = sum(int(d) for d in str(abs(n)))
print("Digit sum:", digit_sum)
print("Digit count:", len(str(abs(n))))
print("Binary:", bin(n) if n >= 0 else "Not available")

if n > 0:
    digits = str(n)
    armstrong_sum = sum(int(d) ** len(digits) for d in digits)
    print("Armstrong:", "Yes" if armstrong_sum == n else "No")
    print("Palindrome:", "Yes" if digits == digits[::-1] else "No")
else:
    print("Armstrong: No")
    print("Palindrome: No")

perfect_sum = 0
for i in range(1, n):
    if n > 0 and n % i == 0:
        perfect_sum += i

print("Perfect number:", "Yes" if n > 0 and perfect_sum == n else "No")