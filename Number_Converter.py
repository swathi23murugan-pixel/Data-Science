n = int(input("Enter a decimal number: "))

print("Binary:", format(n, "b"))
print("Octal:", format(n, "o"))
print("Hexadecimal:", format(n, "X"))

a = int(input("Enter first number for GCD and LCM: "))
b = int(input("Enter second number: "))

x, y = abs(a), abs(b)

while y != 0:
    x, y = y, x % y

gcd = x
lcm = abs(a * b) // gcd if gcd != 0 else 0

print("GCD:", gcd)
print("LCM:", lcm)