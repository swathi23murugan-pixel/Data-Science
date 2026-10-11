a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

if all(ch in "01" for ch in a + b) and a and b:
    x = int(a, 2)
    y = int(b, 2)
    print("Sum:", bin(x + y)[2:])
else:
    print("Enter valid binary numbers")