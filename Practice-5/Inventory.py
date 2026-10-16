products = [("Sensor", 4, 150.0), ("Cable", 12, 25.0), ("Board", 3, 800.0)]
total = 0
low = []
for name, quantity, price in products:
    value = quantity * price
    total += value
    print(name + ": Value = " + format(value, ".2f"))
    if quantity < 5:
        low.append(name)
print("Low-stock products:", low)
print("Total inventory value:", format(total, ".2f"))