try:
    a = int(input("Enter an integer: "))
    b = float(input("Enter a decimal number: "))

    print("Integer:", a)
    print("Type:", type(a))
    print("Decimal:", b)
    print("Type:", type(b))
    print("Rounded value:", round(b))
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Remainder:", a % b)
    print("Power:", a ** 2)

except ValueError:
    print("Enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")