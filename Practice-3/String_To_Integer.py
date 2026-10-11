s = input("Enter a number as a string: ").strip()
result = 0
sign = 1
i = 0

if s and s[0] == "-":
    sign = -1
    i = 1
elif s and s[0] == "+":
    i = 1

valid = i < len(s)

while i < len(s):
    if s[i] < "0" or s[i] > "9":
        valid = False
        break

    result = result * 10 + ord(s[i]) - ord("0")
    i += 1

if valid:
    print("Integer:", result * sign)
else:
    print("Invalid number")