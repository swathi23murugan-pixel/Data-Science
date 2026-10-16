while True:
    print("1. Celsius to Fahrenheit")
    print("2. Kilometres to Miles")
    print("3. Kilograms to Pounds")
    print("4. Exit")
    choice = int(input())
    if choice == 1:
        c = float(input())
        print("Fahrenheit:", round(c * 9 / 5 + 32, 2))
    elif choice == 2:
        km = float(input())
        print("Miles:", round(km * 0.6214, 2))
    elif choice == 3:
        kg = float(input())
        print("Pounds:", round(kg * 2.2046, 2))
    elif choice == 4:
        break
    else:
        print("Invalid choice")
        continue